"""L1 — ORCHESTRATOR: bộ điều phối workflow.

Không phải AI. Chỉ là code điều hành:
  1. Nhận goal            5. Chuyển output agent này sang agent khác (qua state)
  2. Tạo task             6. Retry khi lỗi
  3. Gọi agent            7. Dừng / hỏi người khi cần
  4. Kiểm tra trạng thái  8. Trả artifact cuối + evidence
"""

import hashlib
import json
import shutil
import time
from datetime import datetime
from pathlib import Path

from agents.analyst import AnalystAgent
from agents.base import OutputInvalid
from agents.collector import CollectorAgent
from agents.reporter import ReporterAgent
from config import ACTION_RISK, AUTO_EXECUTE_CONFIDENCE, HUMAN_GOAL, OUTPUTS_DIR
from logger import Tracer
from state import TaskState, load_state, new_state, save_state, state_path
from tools import BudgetExceeded, ModelStub, TransientError

S = TaskState


# ---------------------------------------------------------------- Workflow / DAG
class Task:
    def __init__(self, task_id, agent, depends_on, write):
        self.id = task_id
        self.agent = agent
        self.depends_on = depends_on
        self.write = write            # cách ghi output vào shared state


def _write_collect(state, out):
    state["raw_data"], state["sources"], state["rejected"] = (
        out["raw_data"], out["sources"], out["rejected"])


def _write_analyze(state, out):
    state["analysis"] = out


def _write_report(state, out):
    state["report"] = out["report_path"]
    state["artifact"] = {"path": out["report_path"], "sha256": out["sha256"]}


def build_workflow():
    """Collect → Analyze → Report (DAG đơn giản nhất)."""
    return [
        Task("TASK-001", CollectorAgent(), [], _write_collect),
        Task("TASK-002", AnalystAgent(), ["TASK-001"], _write_analyze),
        Task("TASK-003", ReporterAgent(), ["TASK-002"], _write_report),
    ]


# ---------------------------------------------------------------- Human-in-the-loop
class Human:
    """Kênh hỏi con người.

    mode = "ask"     → hỏi qua terminal (input)
    mode = "approve" → tự đồng ý mọi thứ (--yes)
    mode = "deny"    → không có người trực, từ chối/dừng (--no-input)
    """

    def __init__(self, mode="ask"):
        self.mode = mode

    def decide(self, question, options):
        if self.mode == "approve":
            return options[0]
        if self.mode == "deny":
            return options[-1]
        prompt = f"\n  >>> HUMAN: {question} [{'/'.join(options)}] "
        while True:
            try:
                answer = input(prompt).strip().lower()
            except EOFError:
                return options[-1]
            if answer in options:
                return answer


# ---------------------------------------------------------------- Runtime context
class Context:
    """Thứ orchestrator đưa cho agent khi chạy: run_id, model, log."""

    def __init__(self, run_id, state, tracer, agent_name):
        self.run_id = run_id
        self.model = ModelStub(state, state["goal"]["budget"]["max_model_calls"])
        self._tracer, self._agent = tracer, agent_name

    def log(self, msg):
        self._tracer.info(f"{self._agent.lower()}: {msg}", agent=self._agent)


# ---------------------------------------------------------------- Orchestrator
class Orchestrator:
    def __init__(self, human, faults=None):
        self.human = human
        self.faults = dict(faults or {})   # {"COLLECT": 2} → 2 lần lỗi giả lập đầu tiên
        self.workflow = build_workflow()

    # ---- vòng đời run
    def start(self, goal=None):
        run_id = base = datetime.now().strftime("RUN_%Y%m%d-%H%M%S")
        n = 1
        while state_path(run_id).exists():   # tránh trùng ID khi chạy 2 lần trong 1 giây
            n += 1
            run_id = f"{base}-{n}"
        state = new_state(run_id, goal or HUMAN_GOAL)
        self.tracer = Tracer(run_id)
        self.tracer.banner(f"RUN: {run_id}\nGOAL: {state['goal']['goal']}")
        for t in self.workflow:      # Create tasks
            state["tasks"][t.id] = {"agent": t.agent.name, "state": S.CREATED,
                                    "depends_on": t.depends_on, "attempts": 0, "history": []}
            self._transition(state, t, S.CREATED, init=True)
        save_state(state)
        return self._execute(state)

    def resume(self, run_id):
        state = load_state(run_id)
        self.tracer = Tracer(run_id)
        self.tracer.banner(f"RESUME: {run_id}")
        for t in self.workflow:
            info = state["tasks"][t.id]
            if info["state"] != S.DONE:
                # Chỉ chạy lại task chưa xong — recovery / resumability.
                info.update(state=S.CREATED, attempts=0)
                self.tracer.status(t.agent.name, t.id, S.CREATED, "reset để chạy lại")
            else:
                self.tracer.status(t.agent.name, t.id, S.DONE, "giữ kết quả cũ")
        state["status"] = "RUNNING"
        return self._execute(state)

    def _execute(self, state):
        for task in self.workflow:
            info = state["tasks"][task.id]
            if info["state"] == S.DONE:
                continue
            if not self._deps_done(state, task):
                return self._finish(state, "BLOCKED")
            ok = self._run_task(state, task)
            save_state(state)
            if not ok:
                return self._finish(state, info["state"])
            if not self._decision_gate(state, task):
                return self._finish(state, "STOPPED_BY_HUMAN")
        self._validate_artifact(state)
        self._publish_gate(state)
        return self._finish(state, "SUCCESS")

    # ---- một task với retry
    def _run_task(self, state, task):
        info = state["tasks"][task.id]
        agent = task.agent
        max_retry = state["goal"]["stop_conditions"]["max_retry"]
        if info["state"] != S.QUEUED:
            self._transition(state, task, S.QUEUED)

        while True:
            info["attempts"] += 1
            self._transition(state, task, S.RUNNING,
                             f"attempt {info['attempts']}/{max_retry + 1}")
            started = time.time()
            try:
                inputs = self._resolve_inputs(state, agent)
                self._inject_fault(agent.name)
                output = agent.validate(agent.run(inputs, Context(state["run_id"], state,
                                                                  self.tracer, agent.name)),
                                        inputs)
            except BudgetExceeded as e:
                # Vượt ngân sách: retry không giúp được → đi thẳng lên người.
                self._transition(state, task, S.FAILED, str(e))
                return self._escalate(state, task, f"Vượt ngân sách: {e}", allow_retry=False)
            except (TransientError, OutputInvalid) as e:
                elapsed = time.time() - started
                self._transition(state, task, S.FAILED, f"{type(e).__name__}: {e} ({elapsed:.2f}s)")
                if info["attempts"] <= max_retry:
                    self._transition(state, task, S.RETRYING,
                                     f"retry #{info['attempts']} / max {max_retry}")
                    continue
                return self._escalate(state, task, f"Hết {max_retry} lần retry: {e}")

            task.write(state, output)
            elapsed = time.time() - started
            info["output_summary"] = self._summarize(output)
            self._transition(state, task, S.DONE,
                             f"{info['output_summary']} ({elapsed:.2f}s)")
            return True

    def _escalate(self, state, task, reason, allow_retry=True):
        self._transition(state, task, S.HUMAN_REQUIRED, reason)
        options = ["retry", "abort"] if allow_retry else ["abort"]
        choice = self.human.decide(f"{task.agent.name} cần can thiệp ({reason}). Làm gì?", options)
        self._record_approval(state, f"escalate:{task.id}", choice, reason)
        if choice == "retry":
            state["tasks"][task.id]["attempts"] = 0
            self._transition(state, task, S.QUEUED, "người yêu cầu chạy lại")
            return self._run_task(state, task)
        return False

    # ---- Decision gate: low/medium/high risk + confidence
    def _decision_gate(self, state, task):
        risk = ACTION_RISK.get(task.agent.action, "high")
        confidence = state["analysis"].get("confidence") if task.agent.name == "ANALYZE" else None
        min_conf = state["goal"]["quality"]["min_confidence"]

        if confidence is not None and confidence < min_conf:
            choice = self.human.decide(
                f"Confidence {confidence} < {min_conf}. Tiếp tục tạo báo cáo?", ["yes", "no"])
            self._record_approval(state, f"low_confidence:{task.id}", choice, str(confidence))
            return choice == "yes"
        if risk == "high":
            choice = self.human.decide(f"{task.agent.name} là hành động rủi ro cao. Duyệt?",
                                       ["yes", "no"])
            self._record_approval(state, f"risk:{task.id}", choice, risk)
            return choice == "yes"
        if risk == "medium" or (confidence is not None and confidence < AUTO_EXECUTE_CONFIDENCE):
            self.tracer.info(f"gate: {task.agent.name} risk={risk}"
                             + (f" confidence={confidence}" if confidence is not None else "")
                             + " → tự chạy + ghi log", task_id=task.id)
        return True

    def _publish_gate(self, state):
        """Publish là hành động high risk → luôn phải hỏi người."""
        choice = self.human.decide("Publish báo cáo vào outputs/published/?", ["yes", "no"])
        self._record_approval(state, "publish", choice, ACTION_RISK["publish"])
        if choice == "yes":
            dst = OUTPUTS_DIR / "published" / f"{state['run_id']}_AGENTIC_AI_BRIEF.md"
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(state["report"], dst)
            state["published"] = str(dst)
            self.tracer.info(f"PUBLISHED → {dst.relative_to(OUTPUTS_DIR.parent)}")
        else:
            self.tracer.info("publish: không được duyệt → giữ bản nháp")

    # ---- Artifact / Evidence
    def _validate_artifact(self, state):
        path = Path(state["artifact"]["path"])
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        state["artifact"]["verified"] = actual == state["artifact"]["sha256"]
        self.tracer.info(f"artifact sha256 {'khớp' if state['artifact']['verified'] else 'KHÔNG khớp'}")

    def _write_evidence(self, state):
        out_dir = OUTPUTS_DIR / state["run_id"]
        out_dir.mkdir(parents=True, exist_ok=True)
        evidence = {
            "run_id": state["run_id"],
            "status": state["status"],
            "goal": state["goal"],
            "tasks": {tid: {k: v for k, v in t.items() if k != "history"}
                      for tid, t in state["tasks"].items()},
            "usage": state["usage"],
            "sources": state["sources"],
            "rejected_sources": state.get("rejected", []),
            "approvals": state["approvals"],
            "artifact": state.get("artifact"),
            "published": state.get("published"),
            "trace": str(self.tracer.path),
        }
        path = out_dir / "evidence.json"
        path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
        return path

    def _finish(self, state, status):
        state["status"] = status
        save_state(state)
        evidence = self._write_evidence(state)
        self.tracer.event("run_finished", status=status, usage=state["usage"])
        root = OUTPUTS_DIR.parent
        print(f"\n{'-' * 60}")
        for tid, t in state["tasks"].items():
            print(f"  {tid}  {t['agent']:<8} {t['state']:<14} attempts={t['attempts']}")
        print(f"  model calls: {state['usage']['model_calls']}/"
              f"{state['goal']['budget']['max_model_calls']}")
        if state.get("report"):
            print(f"\nArtifact:\n  {Path(state['report']).relative_to(root)}")
        print(f"Evidence:\n  {evidence.relative_to(root)}\n  {self.tracer.path.relative_to(root)}")
        print(f"\nRUN STATUS:\n  {status}")
        if status != "SUCCESS":
            print(f"\nChạy tiếp từ chỗ dừng:  python main.py --resume {state['run_id']}")
        return state

    # ---- tiện ích
    def _transition(self, state, task, new, detail="", init=False):
        info = state["tasks"][task.id]
        old = info["state"]
        if not init and new not in S.ALLOWED[old]:
            raise RuntimeError(f"{task.id}: chuyển trạng thái sai {old} → {new}")
        info["state"] = new
        info["history"].append({"state": new, "at": datetime.now().isoformat(timespec="seconds"),
                                "detail": detail})
        self.tracer.status(task.agent.name, task.id, new, detail)

    def _deps_done(self, state, task):
        return all(state["tasks"][d]["state"] == S.DONE for d in task.depends_on)

    @staticmethod
    def _resolve_inputs(state, agent):
        """Agent chỉ thấy đúng những key nó khai báo trong contract."""
        inputs = {}
        for key in agent.input_keys:
            if key == "goal":
                inputs[key] = state["goal"]
            elif key in state:
                inputs[key] = state[key]
            else:
                inputs[key] = state["goal"][key]
        return inputs

    def _inject_fault(self, agent_name):
        if self.faults.get(agent_name, 0) > 0:
            self.faults[agent_name] -= 1
            raise TransientError("lỗi giả lập (timeout)")

    def _record_approval(self, state, action, decision, reason):
        entry = {"action": action, "decision": decision, "reason": reason,
                 "by": f"human:{self.human.mode}",
                 "at": datetime.now().isoformat(timespec="seconds")}
        state["approvals"].append(entry)
        self.tracer.event("human_decision", **entry)

    @staticmethod
    def _summarize(output):
        parts = []
        for k, v in output.items():
            if isinstance(v, list):
                parts.append(f"{k}={len(v)}")
            elif isinstance(v, float):
                parts.append(f"{k}={v}")
        return " ".join(parts) or "ok"
