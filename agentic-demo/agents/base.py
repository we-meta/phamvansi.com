"""Agent Contract — "hợp đồng" chung của mọi agent.

Agent
├── Identity      → name, role
├── Goal          → goal
├── Input         → input_keys (đọc từ shared state)
├── Tools         → tools
├── Rules         → rules
├── Output schema → output_schema (kiểm tra trước khi ghi vào state)
├── State         → nhận ctx.state, không giữ state riêng
└── Error policy  → ném TransientError để orchestrator retry
"""


class OutputInvalid(Exception):
    """Output sai schema → coi như task thất bại (có thể retry)."""


class Agent:
    name = "AGENT"
    role = ""
    goal = ""
    input_keys = []
    tools = []
    rules = []
    output_schema = {}          # key → kiểu Python
    action = "research"         # dùng để tra mức rủi ro trong config.ACTION_RISK

    def run(self, inputs, ctx):
        """Thực hiện task. Trả về dict khớp output_schema."""
        raise NotImplementedError

    def validate(self, output, inputs):
        for key, typ in self.output_schema.items():
            if key not in output:
                raise OutputInvalid(f"{self.name}: thiếu trường '{key}'")
            if not isinstance(output[key], typ):
                raise OutputInvalid(f"{self.name}: '{key}' phải là {typ.__name__}")
        self.check_success(output, inputs)
        return output

    def check_success(self, output, inputs):
        """Tiêu chí thành công riêng của từng agent (ghi đè nếu cần)."""

    def describe(self):
        return {"name": self.name, "role": self.role, "goal": self.goal,
                "input": self.input_keys, "tools": self.tools, "rules": self.rules,
                "output": list(self.output_schema)}
