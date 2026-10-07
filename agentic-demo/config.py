"""L0 — HUMAN GOAL: mục tiêu, ràng buộc, tiêu chí chất lượng, ngân sách, quyền hạn.

Đây là nơi con người "ra lệnh". Orchestrator và agent chỉ đọc, không sửa.
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
RUNS_DIR = DATA_DIR / "runs"      # state.json của từng run (để resume)
OUTPUTS_DIR = ROOT / "outputs"    # artifact
LOGS_DIR = ROOT / "logs"          # evidence / trace

HUMAN_GOAL = {
    "goal": "Tìm 5 tin mới về Agentic AI, phân tích ý nghĩa và tạo một bản tóm tắt.",
    "topic": "Agentic AI",
    "constraints": {
        "num_sources": 5,           # Chỉ 5 nguồn
        "min_source_trust": 0.6,    # Nguồn đáng tin cậy
    },
    "quality": {
        "min_confidence": 0.6,      # Dưới ngưỡng → hỏi người
        "required_report_sections": ["Tóm tắt", "Phát hiện chính", "Insight", "Rủi ro", "Nguồn"],
    },
    "budget": {
        "max_model_calls": 10,      # Không quá 10 lần gọi "model"
    },
    "stop_conditions": {
        "max_retry": 2,             # Lỗi quá 2 lần retry → HUMAN_REQUIRED
    },
}

# L1 — HUMAN-IN-THE-LOOP: mức rủi ro của từng hành động.
#   low    → agent tự làm
#   medium → agent tự làm + ghi log
#   high   → phải có người approve
ACTION_RISK = {
    "research": "low",
    "analyze": "low",
    "generate_report": "medium",
    "publish": "high",
    "send_email": "high",
    "spend_money": "high",
}

# Decision gate: kể cả hành động thấp rủi ro, nếu confidence dưới ngưỡng này thì hỏi người.
AUTO_EXECUTE_CONFIDENCE = 0.9
