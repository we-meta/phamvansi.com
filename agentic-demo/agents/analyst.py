"""L2 — AGENT 2: ANALYZE — phân tích dữ liệu.

Bản tối giản dùng luật (rule-based) để lọc, phân loại, tìm insight, đánh giá
độ tin cậy. Khi mở rộng, thay phần thân bằng một lời gọi LLM thật — interface
(input/output schema) giữ nguyên.
"""

from collections import Counter

from agents.base import Agent, OutputInvalid

THEME_INSIGHTS = {
    "orchestration": "Điều phối (DAG, chạy song song, gộp kết quả) đang trở thành lớp hạ tầng riêng.",
    "observability": "Trace, state và log là điều kiện để debug và giảm chi phí chạy lại.",
    "human-in-the-loop": "Phê duyệt của con người cho hành động rủi ro cao đang được chuẩn hoá.",
    "governance": "Quản trị và kiểm toán được đưa vào yêu cầu, không còn là tuỳ chọn.",
    "tools": "Giao thức tool chung giảm chi phí tích hợp agent với hệ thống có sẵn.",
    "enterprise": "Doanh nghiệp áp dụng agent trước ở tác vụ rủi ro thấp, lặp lại nhiều.",
    "cost": "Chi phí model call là rủi ro vận hành cần ngân sách và giới hạn rõ ràng.",
    "reliability": "Thiếu stop condition dẫn tới vòng lặp tốn kém.",
}

RISK_HINTS = {
    "cost": "Chi phí tăng ngoài kiểm soát nếu không có budget/stop condition.",
    "reliability": "Agent có thể lặp vô hạn hoặc thất bại âm thầm.",
    "governance": "Yêu cầu pháp lý có thể đòi log kiểm toán và phê duyệt người.",
    "customer support": "Sai sót khi agent tương tác trực tiếp với khách hàng.",
}


class AnalystAgent(Agent):
    name = "ANALYZE"
    role = "Research analyst"
    goal = "Rút ra phát hiện, insight, rủi ro và mức tin cậy"
    input_keys = ["raw_data", "sources"]
    tools = ["python"]
    rules = ["Chỉ dùng dữ liệu Collector cung cấp", "Mỗi phát hiện phải trỏ về nguồn"]
    output_schema = {"key_findings": list, "insights": list, "risks": list,
                     "categories": dict, "confidence": float}
    action = "analyze"

    def run(self, inputs, ctx):
        ctx.model.call("analyze findings")
        items = inputs["raw_data"]

        findings = [{"text": x["summary"], "source_id": x["id"], "category": x["category"]}
                    for x in items]
        categories = dict(Counter(x["category"] for x in items))

        tags = Counter(t for x in items for t in x["tags"])
        insights = [THEME_INSIGHTS[t] for t, _ in tags.most_common() if t in THEME_INSIGHTS]
        risks = [RISK_HINTS[t] for t, _ in tags.most_common() if t in RISK_HINTS]

        # Độ tin cậy = trung bình trust của nguồn × độ đa dạng góc nhìn (tối đa 4 loại).
        avg_trust = sum(x["trust"] for x in items) / len(items) if items else 0.0
        diversity = min(len(categories), 4) / 4
        confidence = round(avg_trust * (0.7 + 0.3 * diversity), 2)

        ctx.log(f"{len(findings)} phát hiện, {len(insights)} insight, confidence={confidence}")
        return {"key_findings": findings, "insights": insights, "risks": risks,
                "categories": categories, "confidence": confidence}

    def check_success(self, output, inputs):
        if not output["key_findings"]:
            raise OutputInvalid("ANALYZE: không có phát hiện nào")
        source_ids = {s["id"] for s in inputs["sources"]}
        for f in output["key_findings"]:
            if f["source_id"] not in source_ids:
                raise OutputInvalid(f"ANALYZE: phát hiện trỏ tới nguồn lạ {f['source_id']}")
