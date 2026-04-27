# Repository Guidelines

## Project Structure & Module Organization
This repository supports seminar material on coding-related projects using stepwise refinement.

- `seminars/2026-04-20-stepwise-refinement/`: material from the seminar on Monday, April 20, 2026.
- `seminars/2026-04-20-stepwise-refinement/declarative_description.md`: natural-language specification of the example.
- `seminars/2026-04-20-stepwise-refinement/compact_solver.py`: compact imperative 8-queens solver.
- `seminars/2026-04-20-stepwise-refinement/board_solver.py`: more explicit solver with board rendering.
- `pyproject.toml`: project metadata and Python version requirement (`>=3.14`).
- `uv.lock`: locked environment metadata for `uv`.

Keep seminar examples small and readable. New seminar sessions should usually get their own dated subfolder under `seminars/`.

## Build, Test, and Development Commands
- `uv run python seminars/2026-04-20-stepwise-refinement/compact_solver.py`: run the compact solver and print raw solutions.
- `uv run python seminars/2026-04-20-stepwise-refinement/board_solver.py`: run the rendered board solver and print all solutions.
- `uv run python -m py_compile seminars/2026-04-20-stepwise-refinement/*.py`: quick syntax validation for the seminar code.

There is no separate build step or configured test runner yet.

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
This repository does not yet include automated tests. For now, validate changes by running the seminar scripts and checking that they still enumerate valid solutions. When adding tests:

- create files under `tests/` named `test_<feature>.py`
- cover both solver correctness and output-independent logic
- prefer deterministic assertions such as solution counts or attack checks
- when useful, test the declarative description indirectly by asserting the observable behavior promised by that description

## Commit & Pull Request Guidelines
Git history is minimal and only shows a short subject (`first commit`), so keep commit messages concise and imperative, for example: `Add shared solver helper`.

Pull requests should state the seminar goal, the declarative idea being demonstrated, the concrete implementation added, and how it was verified. Include sample commands when behavior is script-visible.
