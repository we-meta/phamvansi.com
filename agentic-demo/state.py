"""L1 — STATE / MEMORY: bộ nhớ dùng chung giữa các agent.

Bản tối giản chỉ là một dict. Ta lưu nó ra JSON sau mỗi bước để có thể
resume (chạy lại đúng bước bị lỗi thay vì chạy lại toàn bộ).
"""

import json
from datetime import datetime

from config import RUNS_DIR


class TaskState:
    """Task state machine.

    CREATED → QUEUED → RUNNING → DONE
                          ↓
                        FAILED → RETRYING → RUNNING ...
                          ↓ (hết lượt retry)
                     HUMAN_REQUIRED
    """

    CREATED = "CREATED"
    QUEUED = "QUEUED"
    RUNNING = "RUNNING"
    DONE = "DONE"
    FAILED = "FAILED"
    RETRYING = "RETRYING"
    HUMAN_REQUIRED = "HUMAN_REQUIRED"
    SKIPPED = "SKIPPED"

    ALLOWED = {
        CREATED: {QUEUED},
        QUEUED: {RUNNING, SKIPPED},
        RUNNING: {DONE, FAILED},
        FAILED: {RETRYING, HUMAN_REQUIRED},
        RETRYING: {RUNNING},
        HUMAN_REQUIRED: {QUEUED, SKIPPED},  # người quyết định: chạy lại hoặc bỏ qua
        DONE: set(),
        SKIPPED: set(),
    }


def new_state(run_id, human_goal):
    return {
        "run_id": run_id,
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "goal": human_goal,
        "status": "RUNNING",          # trạng thái của cả run
        "tasks": {},                  # task_id → {agent, state, attempts, ...}
        "usage": {"model_calls": 0},
        # Dữ liệu chảy qua các agent:
        "raw_data": [],               # Collector  → state["raw_data"]
        "sources": [],
        "analysis": {},               # Analyst    → state["analysis"]
        "report": "",                 # Reporter   → state["report"] (đường dẫn artifact)
        "approvals": [],              # quyết định của con người
    }


def state_path(run_id):
    return RUNS_DIR / run_id / "state.json"


def save_state(state):
    path = state_path(state["run_id"])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def load_state(run_id):
    return json.loads(state_path(run_id).read_text(encoding="utf-8"))
