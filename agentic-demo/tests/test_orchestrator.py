"""Chạy: python -m unittest discover -s tests"""

import contextlib
import copy
import io
import json
import shutil
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from config import HUMAN_GOAL, LOGS_DIR, OUTPUTS_DIR, RUNS_DIR  # noqa: E402
from orchestrator import Human, Orchestrator  # noqa: E402


class OrchestratorTest(unittest.TestCase):
    def setUp(self):
        self.run_ids = []

    def tearDown(self):
        for rid in self.run_ids:
            shutil.rmtree(RUNS_DIR / rid, ignore_errors=True)
            shutil.rmtree(OUTPUTS_DIR / rid, ignore_errors=True)
            (LOGS_DIR / f"{rid}.jsonl").unlink(missing_ok=True)
            (OUTPUTS_DIR / "published" / f"{rid}_AGENTIC_AI_BRIEF.md").unlink(missing_ok=True)

    def run_quiet(self, fn, *args):
        with contextlib.redirect_stdout(io.StringIO()):
            state = fn(*args)
        self.run_ids.append(state["run_id"])
        return state

    def test_happy_path_produces_verified_artifact(self):
        state = self.run_quiet(Orchestrator(Human("approve")).start)
        self.assertEqual(state["status"], "SUCCESS")
        self.assertEqual(len(state["sources"]), 5)
        self.assertTrue(state["artifact"]["verified"])
        self.assertTrue(Path(state["published"]).exists())
        evidence = json.loads((OUTPUTS_DIR / state["run_id"] / "evidence.json").read_text())
        self.assertEqual(evidence["usage"]["model_calls"], 3)

    def test_low_trust_source_is_rejected(self):
        state = self.run_quiet(Orchestrator(Human("approve")).start)
        self.assertNotIn("N07", [s["id"] for s in state["sources"]])
        self.assertIn("N07", [r["id"] for r in state["rejected"]])

    def test_transient_failure_is_retried(self):
        state = self.run_quiet(Orchestrator(Human("approve"), faults={"COLLECT": 2}).start)
        self.assertEqual(state["status"], "SUCCESS")
        self.assertEqual(state["tasks"]["TASK-001"]["attempts"], 3)

    def test_retry_exhausted_then_resume_only_failed_task(self):
        state = self.run_quiet(Orchestrator(Human("deny"), faults={"REPORT": 9}).start)
        self.assertEqual(state["status"], "HUMAN_REQUIRED")
        self.assertEqual(state["tasks"]["TASK-003"]["state"], "HUMAN_REQUIRED")
        calls_before = state["usage"]["model_calls"]

        resumed = self.run_quiet(Orchestrator(Human("approve")).resume, state["run_id"])
        self.assertEqual(resumed["status"], "SUCCESS")
        self.assertEqual(resumed["tasks"]["TASK-001"]["attempts"], 1)   # không chạy lại
        self.assertEqual(resumed["usage"]["model_calls"], calls_before + 1)

    def test_publish_requires_approval(self):
        state = self.run_quiet(Orchestrator(Human("deny")).start)
        self.assertEqual(state["status"], "SUCCESS")
        self.assertNotIn("published", state)
        self.assertEqual(state["approvals"][-1]["decision"], "no")

    def test_budget_exceeded_escalates_without_retry(self):
        goal = copy.deepcopy(HUMAN_GOAL)
        goal["budget"]["max_model_calls"] = 1
        state = self.run_quiet(Orchestrator(Human("deny")).start, goal)
        self.assertEqual(state["status"], "HUMAN_REQUIRED")
        self.assertEqual(state["tasks"]["TASK-002"]["attempts"], 1)


if __name__ == "__main__":
    unittest.main()
