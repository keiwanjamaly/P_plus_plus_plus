"""
Intentionally clumsy tests for the seminar.

They work, but each one has to carry far more setup than the behavior under
test really deserves.
"""

import sys
import unittest
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("simulation.py")
SPEC = importlib.util.spec_from_file_location("testing_done_right_bad_simulation", MODULE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
simulation = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = simulation
SPEC.loader.exec_module(simulation)

run_simulation = simulation.run_simulation


class TestSimulation(unittest.TestCase):
    def test_full_report_has_to_be_asserted_as_text(self) -> None:
        config = {
            "problem": {
                "name": "case-1",
                "difficulty": "hard",
                "mode": "demo",
            },
            "discretization": {
                "method": "adaptive",
                "cells": 8,
                "order": 2,
                "limiter": "soft",
            },
            "time": {
                "steps": 4,
                "dt": 0.25,
                "scheme": "implicit",
                "safety_factor": 0.5,
            },
            "output": {
                "include_history": True,
                "include_config": False,
                "uppercase": False,
            },
        }

        expected = "\n".join(
            [
                "Simulation Report",
                "name=case-1",
                "difficulty=hard",
                "method=adaptive",
                "cells=8",
                "order=2",
                "stencil_width=5",
                "steps=4",
                "dt=0.25",
                "scheme=implicit",
                "score=6.5",
                "history:",
                "step=0,value=6.5,scheme=implicit,mode=demo",
                "step=1,value=6.6,scheme=implicit,mode=demo",
                "step=2,value=6.7,scheme=implicit,mode=demo",
                "step=3,value=6.8,scheme=implicit,mode=demo",
            ]
        )

        self.assertEqual(run_simulation(config), expected)

    def test_uppercase_mode_forces_another_large_report_assertion(self) -> None:
        config = {
            "problem": {
                "name": "case-1",
                "difficulty": "hard",
                "mode": "demo",
            },
            "discretization": {
                "method": "adaptive",
                "cells": 8,
                "order": 2,
                "limiter": "soft",
            },
            "time": {
                "steps": 4,
                "dt": 0.25,
                "scheme": "implicit",
                "safety_factor": 0.5,
            },
            "output": {
                "include_history": True,
                "include_config": False,
                "uppercase": True,
            },
        }

        result = run_simulation(config)
        self.assertEqual(
            result,
            "\n".join(
                [
                    "SIMULATION REPORT",
                    "NAME=CASE-1",
                    "DIFFICULTY=HARD",
                    "METHOD=ADAPTIVE",
                    "CELLS=8",
                    "ORDER=2",
                    "STENCIL_WIDTH=5",
                    "STEPS=4",
                    "DT=0.25",
                    "SCHEME=IMPLICIT",
                    "SCORE=6.5",
                    "HISTORY:",
                    "STEP=0,VALUE=6.5,SCHEME=IMPLICIT,MODE=DEMO",
                    "STEP=1,VALUE=6.6,SCHEME=IMPLICIT,MODE=DEMO",
                    "STEP=2,VALUE=6.7,SCHEME=IMPLICIT,MODE=DEMO",
                    "STEP=3,VALUE=6.8,SCHEME=IMPLICIT,MODE=DEMO",
                ]
            ),
        )

    def test_discretization_detail_still_needs_the_full_configuration_blob(self) -> None:
        # Even though the point is only the stencil width, this test still has
        # to go through the whole simulation config and inspect rendered text.
        config = {
            "problem": {
                "name": "discretization-case",
                "difficulty": "normal",
                "mode": "analysis",
            },
            "discretization": {
                "method": "adaptive",
                "cells": 6,
                "order": 3,
                "limiter": "off",
            },
            "time": {
                "steps": 2,
                "dt": 0.1,
                "scheme": "explicit",
                "safety_factor": 1.0,
            },
            "output": {
                "include_history": False,
                "include_config": False,
                "uppercase": False,
            },
        }

        result = run_simulation(config)
        self.assertIn("name=discretization-case", result)
        self.assertIn("method=adaptive", result)
        self.assertIn("stencil_width=7", result)
        self.assertIn("score=4.4", result)


if __name__ == "__main__":
    unittest.main()
