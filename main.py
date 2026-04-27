from dataclasses import dataclass
from enum import Enum, StrEnum


class Difficulty(Enum):
    EASY = 0
    NORMAL = 1
    HARD = 2


@dataclass(frozen=True)
class Problem:
    name: str
    difficulty: Difficulty = Difficulty.NORMAL
    mode: str = "demo"


print(Problem("Problem 1", Difficulty.EASY))
