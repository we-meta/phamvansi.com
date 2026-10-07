"""Entry point: python main.py

Ví dụ:
  python main.py                         # chạy, hỏi người ở các điểm cần duyệt
  python main.py --yes                   # tự đồng ý mọi phê duyệt
  python main.py --fail COLLECT=1 --yes  # giả lập lỗi → thấy retry
  python main.py --fail REPORT=9 --no-input   # lỗi quá retry → HUMAN_REQUIRED, dừng
  python main.py --resume RUN_xxx --yes  # chạy tiếp, chỉ chạy lại task chưa DONE
  python main.py --describe              # in "hợp đồng" của các agent
"""

import argparse
import json
import sys

from orchestrator import Human, Orchestrator, build_workflow


def parse_faults(values):
    faults = {}
    for v in values or []:
        name, _, count = v.partition("=")
        faults[name.upper()] = int(count or 1)
    return faults


def main(argv=None):
    p = argparse.ArgumentParser(description="Agentic Orchestration tối giản")
    p.add_argument("--yes", action="store_true", help="tự đồng ý mọi phê duyệt của con người")
    p.add_argument("--no-input", action="store_true", help="không có người trực: từ chối / dừng")
    p.add_argument("--fail", action="append", metavar="AGENT=N",
                   help="giả lập N lần lỗi tạm thời cho agent (COLLECT, ANALYZE, REPORT)")
    p.add_argument("--resume", metavar="RUN_ID", help="chạy tiếp một run đã dừng")
    p.add_argument("--describe", action="store_true", help="in agent contract rồi thoát")
    args = p.parse_args(argv)

    if args.describe:
        for t in build_workflow():
            print(t.id, json.dumps(t.agent.describe(), ensure_ascii=False, indent=2))
        return 0

    mode = "approve" if args.yes else "deny" if args.no_input else "ask"
    orch = Orchestrator(Human(mode), faults=parse_faults(args.fail))
    state = orch.resume(args.resume) if args.resume else orch.start()
    return 0 if state["status"] == "SUCCESS" else 1


if __name__ == "__main__":
    sys.exit(main())
