# Testing Done Right

This seminar contrasts two designs for the same toy problem.

- `bad/` shows a design where one nested configuration blob is the API, parsing and computation are mixed together, and the only result is a formatted report string.
- `good/` shows the same behavior with explicit domain concepts, separate parsing, and focused test seams.

The point is not that the bad code is ugly. The point is that its design makes testing awkward:

- to test one discretization detail, the test still has to construct the whole simulation configuration
- the tests can only observe behavior through brittle text output
- there is no local concept to test directly, so the tests become broad and repetitive

Compare these files directly:

- `bad/tests.py`
- `good/tests.py`
- `good/discretization_tests.py`

Run the seminar examples from the repository root:

```bash
uv run python -m unittest seminars/2026-04-27-testing-done-right/bad/tests.py
uv run python -m unittest seminars/2026-04-27-testing-done-right/good/tests.py
uv run python -m unittest seminars/2026-04-27-testing-done-right/good/discretization_tests.py
```

The key takeaway is:

bad design -> hidden concepts -> large brittle tests

good design -> explicit concepts -> small focused tests
