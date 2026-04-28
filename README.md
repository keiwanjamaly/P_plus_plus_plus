# P plus plus plus

This repository collects seminar material about coding-related projects.
Current topics include stepwise refinement and how design choices affect
testability.

## Current seminars

- [2026-04-20 Stepwise Refinement](seminars/2026-04-20-stepwise-refinement/README.md)
- [2026-04-27 Testing Done Right](seminars/2026-04-27-testing-done-right/README.md)

## Running the examples

```bash
uv run python seminars/2026-04-20-stepwise-refinement/compact_solver.py
uv run python seminars/2026-04-20-stepwise-refinement/board_solver.py
uv run python -m unittest seminars/2026-04-27-testing-done-right/bad/tests.py
uv run python -m unittest seminars/2026-04-27-testing-done-right/good/tests.py
uv run python -m unittest seminars/2026-04-27-testing-done-right/good/discretization_tests.py
```

The current examples cover two complementary themes:

- the eight queens problem for stepwise refinement
- a paired bad/good toy codebase that shows how design choices directly affect testability
