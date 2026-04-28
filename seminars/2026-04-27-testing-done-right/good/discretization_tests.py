"""
Focused tests for the discretization concept.

These are useful in the seminar because they show that we do not need to go
through the full simulation runner to test discretization behavior.
"""

import sys
import unittest
import importlib.util
from pathlib import Path

MODULE_PATH = Path(__file__).with_name("simulation.py")
SPEC = importlib.util.spec_from_file_location("testing_done_right_good_simulation_discretization", MODULE_PATH)
assert SPEC is not None
assert SPEC.loader is not None
simulation = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = simulation
SPEC.loader.exec_module(simulation)

Discretization = simulation.Discretization
DiscretizationMethod = simulation.DiscretizationMethod
Limiter = simulation.Limiter
validate_discretization = simulation.validate_discretization


class TestDiscretization(unittest.TestCase):
    def test_uniform_discretization_keeps_cell_count(self) -> None:
        discretization = Discretization(
            method=DiscretizationMethod.UNIFORM,
            cells=8,
            order=2,
        )

        self.assertEqual(discretization.effective_cells(), 8)

    def test_adaptive_discretization_changes_effective_cell_count(self) -> None:
        discretization = Discretization(
            method=DiscretizationMethod.ADAPTIVE,
            cells=8,
            order=2,
        )

        self.assertEqual(discretization.effective_cells(), 16)

    def test_stencil_width_depends_only_on_order(self) -> None:
        discretization = Discretization(
            method=DiscretizationMethod.UNIFORM,
            cells=8,
            order=3,
            limiter=Limiter.STRICT,
        )

        self.assertEqual(discretization.stencil_width(), 7)

    def test_invalid_discretization_is_rejected_locally(self) -> None:
        discretization = Discretization(
            method=DiscretizationMethod.UNIFORM,
            cells=0,
            order=2,
        )

        with self.assertRaises(ValueError):
            validate_discretization(discretization)


if __name__ == "__main__":
    unittest.main()
