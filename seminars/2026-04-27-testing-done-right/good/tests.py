import sys
import unittest
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("simulation.py")
SPEC = importlib.util.spec_from_file_location("testing_done_right_good_simulation", MODULE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
simulation = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = simulation
SPEC.loader.exec_module(simulation)

Difficulty = simulation.Difficulty
Discretization = simulation.Discretization
DiscretizationMethod = simulation.DiscretizationMethod
Limiter = simulation.Limiter
Problem = simulation.Problem
Simulation = simulation.Simulation
TimeScheme = simulation.TimeScheme
TimeStepper = simulation.TimeStepper
parse_simulation = simulation.parse_simulation
run_simulation = simulation.run_simulation


def make_simulation(
    *,
    difficulty: Difficulty = Difficulty.NORMAL,
    method: DiscretizationMethod = DiscretizationMethod.UNIFORM,
    cells: int = 10,
    order: int = 1,
    limiter: Limiter = Limiter.OFF,
    steps: int = 3,
    dt: float = 0.1,
    scheme: TimeScheme = TimeScheme.EXPLICIT,
    safety_factor: float = 1.0,
) -> Simulation:
    return Simulation(
        problem=Problem(name="case", difficulty=difficulty),
        discretization=Discretization(
            method=method,
            cells=cells,
            order=order,
            limiter=limiter,
        ),
        time_stepper=TimeStepper(
            steps=steps,
            dt=dt,
            scheme=scheme,
            safety_factor=safety_factor,
        ),
    )


class TestSimulation(unittest.TestCase):
    def test_adaptive_implicit_configuration_produces_expected_score(self) -> None:
        simulation = make_simulation(
            difficulty=Difficulty.HARD,
            method=DiscretizationMethod.ADAPTIVE,
            cells=8,
            order=2,
            limiter=Limiter.SOFT,
            steps=4,
            dt=0.25,
            scheme=TimeScheme.IMPLICIT,
            safety_factor=0.5,
        )

        result = run_simulation(simulation)

        self.assertEqual(result.score, 6.5)

    def test_history_contains_one_entry_per_step(self) -> None:
        simulation = make_simulation(steps=4)

        result = run_simulation(simulation)

        self.assertEqual(result.history, (2.4, 2.5, 2.6, 2.7))

    def test_negative_cell_count_is_rejected(self) -> None:
        simulation = make_simulation(cells=-1)

        with self.assertRaises(ValueError):
            run_simulation(simulation)

    def test_parser_is_a_separate_concern(self) -> None:
        simulation = parse_simulation(
            {
                "problem": {"name": "parsed", "difficulty": "easy"},
                "discretization": {"method": "adaptive", "cells": 5, "order": 2},
                "time": {"steps": 2, "dt": 0.5, "scheme": "explicit"},
            }
        )

        self.assertEqual(simulation.problem.name, "parsed")
        self.assertEqual(simulation.problem.difficulty, Difficulty.EASY)
        self.assertEqual(simulation.discretization.method, DiscretizationMethod.ADAPTIVE)


if __name__ == "__main__":
    unittest.main()
