"""
Cleaner reference version for the "Testing done right" seminar.

Intended behavior:
- model the relevant concepts explicitly
- keep parsing separate from the domain logic
- return structured results instead of formatted text
"""

from dataclasses import dataclass
from enum import StrEnum
from typing import Any


class Difficulty(StrEnum):
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"


class DiscretizationMethod(StrEnum):
    UNIFORM = "uniform"
    ADAPTIVE = "adaptive"


class Limiter(StrEnum):
    OFF = "off"
    SOFT = "soft"
    STRICT = "strict"


class TimeScheme(StrEnum):
    EXPLICIT = "explicit"
    IMPLICIT = "implicit"


@dataclass(frozen=True)
class Problem:
    name: str
    difficulty: Difficulty = Difficulty.NORMAL
    mode: str = "demo"


@dataclass(frozen=True)
class Discretization:
    method: DiscretizationMethod
    cells: int
    order: int
    limiter: Limiter = Limiter.OFF

    def effective_cells(self) -> int:
        if self.method is DiscretizationMethod.ADAPTIVE:
            return self.cells * 2
        return self.cells

    def stencil_width(self) -> int:
        return 2 * self.order + 1


@dataclass(frozen=True)
class TimeStepper:
    steps: int
    dt: float
    scheme: TimeScheme
    safety_factor: float = 1.0


@dataclass(frozen=True)
class Simulation:
    problem: Problem
    discretization: Discretization
    time_stepper: TimeStepper


@dataclass(frozen=True)
class SimulationResult:
    score: float
    history: tuple[float, ...]


def validate_discretization(discretization: Discretization) -> None:
    if discretization.cells <= 0:
        raise ValueError("cells must be positive")
    if discretization.order <= 0:
        raise ValueError("order must be positive")


def validate_time_stepper(time_stepper: TimeStepper) -> None:
    if time_stepper.steps < 0:
        raise ValueError("steps must be non-negative")
    if time_stepper.dt <= 0:
        raise ValueError("dt must be positive")


def run_simulation(simulation: Simulation) -> SimulationResult:
    validate_discretization(simulation.discretization)
    validate_time_stepper(simulation.time_stepper)

    difficulty_penalty = {
        Difficulty.EASY: -1,
        Difficulty.NORMAL: 0,
        Difficulty.HARD: 2,
    }[simulation.problem.difficulty]

    cell_factor = simulation.discretization.effective_cells()

    scheme_factor = {
        TimeScheme.EXPLICIT: 1,
        TimeScheme.IMPLICIT: 3,
    }[simulation.time_stepper.scheme]

    limiter_factor = {
        Limiter.OFF: 0,
        Limiter.SOFT: 2,
        Limiter.STRICT: 5,
    }[simulation.discretization.limiter]

    raw_score = (
        cell_factor
        + simulation.discretization.order * 10
        + simulation.time_stepper.steps * scheme_factor
        + limiter_factor
        + difficulty_penalty
    )
    score = raw_score * simulation.time_stepper.dt * simulation.time_stepper.safety_factor

    history = tuple(round(score + step / 10, 3) for step in range(simulation.time_stepper.steps))
    return SimulationResult(score=round(score, 3), history=history)


def parse_simulation(config: dict[str, Any]) -> Simulation:
    problem = config.get("problem", {})
    discretization = config.get("discretization", {})
    time = config.get("time", {})

    return Simulation(
        problem=Problem(
            name=problem.get("name", "unnamed"),
            difficulty=Difficulty(problem.get("difficulty", "normal")),
            mode=problem.get("mode", "demo"),
        ),
        discretization=Discretization(
            method=DiscretizationMethod(discretization.get("method", "uniform")),
            cells=discretization.get("cells", 10),
            order=discretization.get("order", 1),
            limiter=Limiter(discretization.get("limiter", "off")),
        ),
        time_stepper=TimeStepper(
            steps=time.get("steps", 3),
            dt=time.get("dt", 0.1),
            scheme=TimeScheme(time.get("scheme", "explicit")),
            safety_factor=time.get("safety_factor", 1.0),
        ),
    )


if __name__ == "__main__":
    simulation = Simulation(
        problem=Problem(name="seminar-demo", difficulty=Difficulty.HARD),
        discretization=Discretization(
            method=DiscretizationMethod.ADAPTIVE,
            cells=8,
            order=2,
            limiter=Limiter.SOFT,
        ),
        time_stepper=TimeStepper(
            steps=4,
            dt=0.25,
            scheme=TimeScheme.IMPLICIT,
            safety_factor=0.5,
        ),
    )
    print(run_simulation(simulation))
