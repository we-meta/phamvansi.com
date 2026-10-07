# agentic-demo — Agentic Orchestration tối giản

Dự án học tập: một hệ điều phối Human × Agent nhỏ nhất có thể chạy được, viết bằng
Python thuần (không cần cài thư viện, chạy offline).

Nhiệm vụ mẫu: *“Tìm 5 tin mới về Agentic AI, phân tích ý nghĩa và tạo một bản tóm tắt.”*

> Dữ liệu trong `data/sample_news.json` là **dữ liệu mẫu (mock)**, không phải tin thật.
> "Model" là `ModelStub` (chỉ đếm số lần gọi). Thay bằng web search và LLM thật khi mở rộng.

## Chạy thử

```bash
cd agentic-demo
python main.py                             # hỏi anh ở các điểm cần duyệt (publish...)
python main.py --yes                       # tự đồng ý mọi phê duyệt
python main.py --fail COLLECT=1 --yes      # giả lập lỗi → thấy RETRYING
python main.py --fail REPORT=9 --no-input  # lỗi quá max_retry → HUMAN_REQUIRED, dừng
python main.py --resume RUN_xxx --yes      # chạy tiếp: chỉ chạy lại task chưa DONE
python main.py --describe                  # in "hợp đồng" (contract) của từng agent
python -m unittest discover -s tests       # test
```

Terminal:

```
[04:47:10] TASK-001  COLLECT  RUNNING        attempt 1/3
[04:47:10] TASK-001  COLLECT  FAILED         TransientError: lỗi giả lập (timeout)
[04:47:10] TASK-001  COLLECT  RETRYING       retry #1 / max 2
[04:47:10] TASK-001  COLLECT  RUNNING        attempt 2/3
[04:47:10] TASK-001  COLLECT  DONE           sources=5 raw_data=5 rejected=1
[04:47:10] TASK-002  ANALYZE  RUNNING        attempt 1/3
[04:47:10] TASK-002  ANALYZE  DONE           key_findings=5 insights=6 risks=2 confidence=0.88
[04:47:10] TASK-003  REPORT   RUNNING        attempt 1/3
[04:47:10] TASK-003  REPORT   DONE           sections=5
...
RUN STATUS:
  SUCCESS
```

## Phân cấp → file

```
L0 — HUMAN GOAL ............ config.py        goal, constraints, quality, budget, stop conditions, mức rủi ro
│
├── L1 — ORCHESTRATOR ...... orchestrator.py  workflow (DAG), gọi agent, state machine, retry, decision gate
│   ├── L2 — COLLECT ....... agents/collector.py
│   ├── L2 — ANALYZE ....... agents/analyst.py
│   └── L2 — REPORT ........ agents/reporter.py
│        (contract chung) .. agents/base.py
│
├── L1 — STATE / MEMORY .... state.py         shared state + lưu data/runs/<RUN_ID>/state.json
├── L1 — LOG / TRACE ....... logger.py        terminal + logs/<RUN_ID>.jsonl
├── L1 — ERROR / RETRY ..... orchestrator.py  max_retry, BudgetExceeded, resume
├── L1 — HUMAN-IN-THE-LOOP . orchestrator.py  class Human + _decision_gate + _publish_gate
├── L1 — ARTIFACT / EVIDENCE outputs/<RUN_ID>/AGENTIC_AI_BRIEF.md + evidence.json (sha256)
│
└── Tool / Model layer ..... tools.py         web_search (offline), write_file, ModelStub (budget)
```

## Các khái niệm trong code

| Khái niệm | Ở đâu | Ghi chú |
|---|---|---|
| Agent contract | `agents/base.py` | Identity, Goal, Input, Tools, Rules, Output schema, Error policy |
| Agent ≠ Task | `orchestrator.py` → `Task` | Task = công việc (`TASK-001`), agent = người làm |
| State machine | `state.py` → `TaskState` | CREATED → QUEUED → RUNNING → DONE / FAILED → RETRYING → HUMAN_REQUIRED; chuyển sai sẽ báo lỗi |
| DAG | `build_workflow()` | `depends_on`; Collect → Analyze → Report |
| Shared state | `state.py` | Collector → `raw_data`, Analyst → `analysis`, Reporter → `report` |
| Observability / trace | `logger.py` | Mỗi sự kiện có `run_id`, `task_id`, `agent`, `state`, thời gian |
| Retry | `_run_task` | `max_retry = 2`; lỗi tạm thời và output sai schema được retry |
| Budget | `tools.ModelStub` | Vượt `max_model_calls` → không retry, chuyển thẳng cho người |
| Resumability | `--resume` | Task đã DONE giữ nguyên, chỉ chạy lại phần lỗi |
| Decision gate | `_decision_gate` | low → tự làm; medium → tự làm + log; high hoặc confidence thấp → hỏi người |
| Evidence | `evidence.json` | Nguồn, nguồn bị loại, số lần thử, quyết định của người, sha256 của artifact |

## Lần ngược khi báo cáo sai

```
Report sai → outputs/<RUN_ID>/evidence.json   (artifact, nguồn, approvals)
           → data/runs/<RUN_ID>/state.json    (analysis, raw_data)
           → logs/<RUN_ID>.jsonl              (từng bước, từng lần retry)
```

## Mở rộng dần

1. Thay `tools.web_search` bằng search API thật; thay `ModelStub` bằng LLM thật (giữ nguyên output schema).
2. Thêm collector song song (paper / news / market) → `depends_on` nhiều nhánh, chạy bằng `concurrent.futures`.
3. Tách Technical / Business analysis rồi gộp ở Reporter.
4. Thêm token usage / cost vào trace.
5. Dynamic routing: để orchestrator chọn agent theo goal.
