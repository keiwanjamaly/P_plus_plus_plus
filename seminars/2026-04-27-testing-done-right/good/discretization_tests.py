"""
Focused tests for the discretization concept.

These are useful in the seminar because they show that we do not need to go
through the full simulation runner to test discretization behavior.
"""

import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from simulation import (
    Discretization,
    DiscretizationMethod,
    Limiter,
    validate_discretization,
)


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
