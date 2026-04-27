from dataclasses import dataclass
from enum import StrEnum
from typing import Any


class Difficulty(StrEnum):
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"


def run_simulation(config: dict[str, Any]) -> str:
    config.setdefault("problem", {})
    config.setdefault("discretization", {})
    config.setdefault("time", {})
    config.setdefault("output", {})

    problem = config["problem"]
    discretization = config["discretization"]
    time = config["time"]
    output = config["output"]

    name = problem.get("name", "unnamed")
    difficulty = Difficulty.HARD
    difficulty = problem.get("difficulty", "normal")
    mode = problem.get("mode", "demo")

    method = discretization.get("method", "uniform")
    cells = discretization.get("cells", 10)
    order = discretization.get("order", 1)
    limiter = discretization.get("limiter", "off")

    steps = time.get("steps", 3)
    dt = time.get("dt", 0.1)
    scheme = time.get("scheme", "explicit")
    safety_factor = time.get("safety_factor", 1.0)

    include_history = output.get("include_history", True)
    include_config = output.get("include_config", True)
    uppercase = output.get("uppercase", False)

    if cells <= 0:
        raise ValueError("cells must be positive")
    if order <= 0:
        raise ValueError("order must be positive")
    if steps < 0:
        raise ValueError("steps must be non-negative")
    if dt <= 0:
        raise ValueError("dt must be positive")

    if difficulty == "hard":
        penalty = 2
    elif difficulty == "easy":
        penalty = -1
    else:
        penalty = 0

    if method == "adaptive":
        cell_factor = cells * 2
    else:
        cell_factor = cells

    if scheme == "implicit":
        scheme_factor = 3
    else:
        scheme_factor = 1

    if limiter == "strict":
        limiter_factor = 5
    elif limiter == "soft":
        limiter_factor = 2
    else:
        limiter_factor = 0

    raw_score = (
        cell_factor + order * 10 + steps * scheme_factor + limiter_factor + penalty
    )
    scaled_score = raw_score * dt * safety_factor

    history: list[str] = []
    for step in range(steps):
        history.append(
            "step="
            + str(step)
            + ",value="
            + str(round(scaled_score + step / 10, 3))
            + ",scheme="
            + scheme
            + ",mode="
            + mode
        )

    report_lines = [
        "Simulation Report",
        "name=" + str(name),
        "difficulty=" + str(difficulty),
        "method=" + str(method),
        "cells=" + str(cells),
        "order=" + str(order),
        "steps=" + str(steps),
        "dt=" + str(dt),
        "scheme=" + str(scheme),
        "score=" + str(round(scaled_score, 3)),
    ]

    if include_history:
        report_lines.append("history:")
        report_lines.extend(history)

    if include_config:
        report_lines.append("config=" + str(config))

    report = "\n".join(report_lines)
    if uppercase:
        report = report.upper()
    return report


if __name__ == "__main__":
    example_config = {
        "problem": {
            "name": "seminar-demo",
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
            "include_config": True,
            "uppercase": False,
        },
    }

    print(run_simulation(example_config))
