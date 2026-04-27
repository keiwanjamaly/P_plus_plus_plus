# Stepwise Refinement Seminar

This folder contains the material for the seminar held on Monday, April 20, 2026. It uses the eight queens problem because that is also the sample problem in Wirth's paper. The seminar adapts that idea into a simple Python-focused workflow:

1. state the problem and constraints clearly
2. refine the solution in small, explicit steps
3. make the control flow and data choices concrete in Python

## Files

- `declarative_description.md`: natural-language version of the algorithm
- `compact_solver.py`: compact imperative solver
- `board_solver.py`: more explicit solver with board rendering

## Run

```bash
uv run python seminars/2026-04-20-stepwise-refinement/compact_solver.py
uv run python seminars/2026-04-20-stepwise-refinement/board_solver.py
```

## Reference

The seminar is inspired by:

Niklaus Wirth, "Program Development by Stepwise Refinement," *Communications of the ACM* 14(4), 221-227, April 1971. DOI: `10.1145/362575.362577`.

Open-access technical-report version:

- ETH Zurich Research Collection: `https://www.research-collection.ethz.ch/handle/20.500.11850/80846`

Important nuance: Wirth's paper is not just "natural language first, code second." It presents program design as a sequence of refinement steps, where task decomposition and data-structure decisions evolve together.
