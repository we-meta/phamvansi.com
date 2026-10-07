"""L1 — LOG / TRACE: quan sát hệ thống.

- Terminal: dòng ngắn, dễ nhìn "agent nào đang chạy".
- logs/<RUN_ID>.jsonl: mỗi sự kiện một dòng JSON (evidence để lần ngược).
"""

import json
import sys
from datetime import datetime

from config import LOGS_DIR

COLORS = {
    "RUNNING": "\033[33m", "DONE": "\033[32m", "FAILED": "\033[31m",
    "RETRYING": "\033[35m", "HUMAN_REQUIRED": "\033[41;97m", "SKIPPED": "\033[90m",
    "QUEUED": "\033[36m", "CREATED": "\033[90m",
}
RESET = "\033[0m"
USE_COLOR = sys.stdout.isatty()


class Tracer:
    def __init__(self, run_id):
        self.run_id = run_id
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        self.path = LOGS_DIR / f"{run_id}.jsonl"

    def event(self, kind, **data):
        record = {"ts": datetime.now().isoformat(timespec="milliseconds"),
                  "run_id": self.run_id, "event": kind, **data}
        with self.path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        return record

    def status(self, agent, task_id, state, detail=""):
        """In một dòng trạng thái và ghi trace."""
        self.event("task_state", agent=agent, task_id=task_id, state=state, detail=detail)
        ts = datetime.now().strftime("%H:%M:%S")
        label = f"{COLORS.get(state, '')}{state:<14}{RESET}" if USE_COLOR else f"{state:<14}"
        line = f"[{ts}] {task_id:<9} {agent:<8} {label}"
        print(line + (f" {detail}" if detail else ""), flush=True)

    def info(self, msg, **data):
        self.event("info", msg=msg, **data)
        print(f"           {msg}", flush=True)

    def banner(self, msg):
        self.event("banner", msg=msg)
        print(f"\n{'=' * 60}\n{msg}\n{'=' * 60}", flush=True)
