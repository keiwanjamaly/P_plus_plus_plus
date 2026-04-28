# Repository Guidelines

## Project Structure & Module Organization
This repository supports seminar material on coding-related projects, currently
covering both stepwise refinement and testability-by-design.

- `seminars/2026-04-20-stepwise-refinement/`: material from the seminar on Monday, April 20, 2026.
- `seminars/2026-04-20-stepwise-refinement/declarative_description.md`: natural-language specification of the example.
- `seminars/2026-04-20-stepwise-refinement/compact_solver.py`: compact imperative 8-queens solver.
- `seminars/2026-04-20-stepwise-refinement/board_solver.py`: more explicit solver with board rendering.
- `seminars/2026-04-27-testing-done-right/`: paired bad/good examples for a seminar on how design choices affect testing difficulty.
- `seminars/2026-04-27-testing-done-right/bad/`: intentionally awkward version where one config blob drives everything.
- `seminars/2026-04-27-testing-done-right/good/`: refactored version with explicit concepts and focused test seams.
- `pyproject.toml`: project metadata and Python version requirement (`>=3.14`).
- `uv.lock`: locked environment metadata for `uv`.

Keep seminar examples small and readable. New seminar sessions should usually get their own dated subfolder under `seminars/`.

## Build, Test, and Development Commands
- `uv run python seminars/2026-04-20-stepwise-refinement/compact_solver.py`: run the compact solver and print raw solutions.
- `uv run python seminars/2026-04-20-stepwise-refinement/board_solver.py`: run the rendered board solver and print all solutions.
- `uv run python -m py_compile seminars/2026-04-20-stepwise-refinement/*.py`: quick syntax validation for the seminar code.
- `uv run python -m unittest seminars/2026-04-27-testing-done-right/bad/tests.py`: run the intentionally clumsy bad-example tests.
- `uv run python -m unittest seminars/2026-04-27-testing-done-right/good/tests.py`: run the good-example simulation tests.
- `uv run python -m unittest seminars/2026-04-27-testing-done-right/good/discretization_tests.py`: run the focused discretization tests.

There is no separate build step. The testing seminar uses plain `unittest`
modules instead of a project-wide test runner.

## Coding Style & Naming Conventions
Follow standard Python conventions:

- Use 4-space indentation and type hints for public functions.
- Prefer `snake_case` for functions and variables.
- Use `PascalCase` for classes such as `Board`.
- Keep functions small and focused.

For seminar work, preserve the declarative-to-imperative flow:

- start each non-trivial exercise with a short natural-language description of the intended behavior
- then implement that behavior in straightforward Python
- prefer clear control flow over clever compression so the mapping from description to code stays obvious
- when relevant, make the intermediate refinement steps explicit instead of jumping directly from idea to finished code

The current codebase is formatter-neutral. If you introduce `ruff` or `pytest`, update this guide and `pyproject.toml` in the same change.

## Testing Guidelines
This repository includes seminar-local automated tests for the testing seminar.
Validate changes by running the relevant seminar scripts or `unittest` modules.
When adding tests:

- prefer keeping seminar-specific tests close to the seminar code when that
  improves readability of the teaching material
- if you add cross-cutting project tests, create files under `tests/` named
  `test_<feature>.py`
- cover both solver correctness and output-independent logic
- prefer deterministic assertions such as solution counts or attack checks
- when useful, test the declarative description indirectly by asserting the observable behavior promised by that description

## Commit & Pull Request Guidelines
Git history is minimal and only shows a short subject (`first commit`), so keep commit messages concise and imperative, for example: `Add shared solver helper`.

Pull requests should state the seminar goal, the declarative idea being demonstrated, the concrete implementation added, and how it was verified. Include sample commands when behavior is script-visible.
