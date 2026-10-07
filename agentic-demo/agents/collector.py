"""L2 — AGENT 1: COLLECT — thu thập dữ liệu."""

from agents.base import Agent, OutputInvalid
from tools import web_search


class CollectorAgent(Agent):
    name = "COLLECT"
    role = "Research collector"
    goal = "Lấy đủ số nguồn hợp lệ về chủ đề"
    input_keys = ["topic", "constraints"]
    tools = ["web_search"]
    rules = ["Không tự phân tích sâu", "Bỏ nguồn dưới ngưỡng tin cậy", "Mới nhất trước"]
    output_schema = {"sources": list, "raw_data": list, "rejected": list}
    action = "research"

    def run(self, inputs, ctx):
        ctx.model.call("rank search results")
        limit = inputs["constraints"]["num_sources"]
        min_trust = inputs["constraints"]["min_source_trust"]

        found = web_search(inputs["topic"])
        accepted = [x for x in found if x["trust"] >= min_trust]
        rejected = [{"id": x["id"], "reason": f"trust {x['trust']} < {min_trust}"}
                    for x in found if x["trust"] < min_trust]
        accepted.sort(key=lambda x: x["date"], reverse=True)
        picked = accepted[:limit]

        ctx.log(f"tìm thấy {len(found)} kết quả, loại {len(rejected)} nguồn kém tin cậy")
        return {
            "sources": [{"id": x["id"], "source": x["source"], "url": x["url"],
                         "date": x["date"], "trust": x["trust"]} for x in picked],
            "raw_data": picked,
            "rejected": rejected,
        }

    def check_success(self, output, inputs):
        # Success: có ít nhất N nguồn hợp lệ.
        if len(output["sources"]) < inputs["constraints"]["num_sources"]:
            raise OutputInvalid(f"COLLECT: chỉ có {len(output['sources'])} nguồn hợp lệ")
