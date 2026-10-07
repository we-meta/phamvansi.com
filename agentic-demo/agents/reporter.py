"""L2 — AGENT 3: REPORT — biến kết quả phân tích thành artifact dễ đọc."""

from agents.base import Agent, OutputInvalid
from config import OUTPUTS_DIR
from tools import write_file


class ReporterAgent(Agent):
    name = "REPORT"
    role = "Report writer"
    goal = "Tạo AGENTIC_AI_BRIEF.md có thể kiểm chứng"
    input_keys = ["goal", "analysis", "sources"]
    tools = ["write_file"]
    rules = ["Mỗi phát hiện kèm mã nguồn [Nxx]", "Không thêm thông tin ngoài analysis"]
    output_schema = {"report_path": str, "sha256": str, "sections": list}
    action = "generate_report"

    def run(self, inputs, ctx):
        ctx.model.call("write brief")
        goal, a, sources = inputs["goal"], inputs["analysis"], inputs["sources"]

        lines = [
            f"# {goal['topic']} — Brief",
            "",
            f"> Run `{ctx.run_id}` · Mục tiêu: {goal['goal']}",
            "> Dữ liệu demo là dữ liệu mẫu (mock), không phải tin thật.",
            "",
            "## Tóm tắt",
            "",
            f"Đã phân tích {len(a['key_findings'])} nguồn thuộc các nhóm "
            + ", ".join(f"{k} ({v})" for k, v in a["categories"].items())
            + f". Độ tin cậy tổng hợp: **{a['confidence']}**.",
            "",
            "## Phát hiện chính",
            "",
            *[f"- {f['text']} [{f['source_id']}]" for f in a["key_findings"]],
            "",
            "## Insight",
            "",
            *[f"- {i}" for i in a["insights"]],
            "",
            "## Rủi ro",
            "",
            *([f"- {r}" for r in a["risks"]] or ["- Chưa ghi nhận."]),
            "",
            "## Nguồn",
            "",
            "| ID | Nguồn | Ngày | Trust | URL |",
            "|----|-------|------|-------|-----|",
            *[f"| {s['id']} | {s['source']} | {s['date']} | {s['trust']} | {s['url']} |"
              for s in sources],
            "",
        ]
        content = "\n".join(lines)
        path = OUTPUTS_DIR / ctx.run_id / "AGENTIC_AI_BRIEF.md"
        sha = write_file(path, content)
        ctx.log(f"ghi {path.relative_to(OUTPUTS_DIR.parent)}")
        sections = [l[3:] for l in lines if l.startswith("## ")]
        return {"report_path": str(path), "sha256": sha, "sections": sections}

    def check_success(self, output, inputs):
        required = inputs["goal"]["quality"]["required_report_sections"]
        missing = [s for s in required if s not in output["sections"]]
        if missing:
            raise OutputInvalid(f"REPORT: thiếu mục {missing}")
