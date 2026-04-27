import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from simulation import run_simulation


class TestSimulation(unittest.TestCase):
    def test_it_works(self) -> None:
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

    def test_it_works_in_uppercase(self) -> None:
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

    def test_stuff(self) -> None:
        config = {
            "problem": {
                "name": "case-2",
                "difficulty": "easy",
                "mode": "analysis",
            },
            "discretization": {
                "method": "uniform",
                "cells": 5,
                "order": 1,
                "limiter": "strict",
            },
            "time": {
                "steps": 2,
                "dt": 0.5,
                "scheme": "explicit",
                "safety_factor": 1.0,
            },
            "output": {
                "include_history": False,
                "include_config": True,
                "uppercase": False,
            },
        }

        result = run_simulation(config)
        self.assertIn("name=case-2", result)
        self.assertIn("difficulty=easy", result)
        self.assertIn("score=10.5", result)
        self.assertIn("config={'problem': {'name': 'case-2'", result)


if __name__ == "__main__":
    unittest.main()
