"""Tool Layer: thứ agent dùng để tác động ra thế giới.

Agent ≠ LLM. Agent = Model + Prompt + State + Tools + Rules + Goal + Runtime.
Ở bản tối giản, mọi tool đều chạy offline và có thể thay bằng tool thật sau.
"""

import hashlib
import json

from config import DATA_DIR


class BudgetExceeded(Exception):
    """Vượt ngân sách do con người đặt → dừng, không retry."""


class TransientError(Exception):
    """Lỗi tạm thời (mạng, timeout...) → đáng để retry."""


class ModelStub:
    """Giả lập một "model call".

    Bản thật sẽ gọi Claude/GPT/Gemini. Ở đây ta chỉ đếm số lần gọi để
    áp dụng budget và ghi vào trace — phần quan sát giống hệt bản thật.
    """

    name = "model-stub-v0"

    def __init__(self, state, max_calls):
        self.state = state
        self.max_calls = max_calls

    def call(self, purpose):
        used = self.state["usage"]["model_calls"]
        if used >= self.max_calls:
            raise BudgetExceeded(f"Đã dùng {used}/{self.max_calls} model calls")
        self.state["usage"]["model_calls"] = used + 1
        return {"model": self.name, "purpose": purpose}


def web_search(topic, path=DATA_DIR / "sample_news.json"):
    """Tool tìm kiếm. Bản demo đọc corpus mẫu cục bộ thay vì gọi Internet."""
    corpus = json.loads(path.read_text(encoding="utf-8"))
    needle = topic.lower()
    return [item for item in corpus["items"]
            if needle in item["title"].lower() or needle in item["tags"]]


def write_file(path, content):
    """Tool ghi file; trả về sha256 làm evidence cho artifact."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return hashlib.sha256(content.encode("utf-8")).hexdigest()
