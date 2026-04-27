# Declarative Description

Goal: place eight queens on a chessboard so that no two queens attack each other.

This file is one refinement stage, not the whole method. In Wirth's presentation, the specification is gradually refined and the data representation evolves alongside the control flow.

Natural-language plan for this seminar version:

1. Work from the first column to the last column.
2. In each column, try every row that is still free.
3. Before placing a queen, check whether an already placed queen attacks that position diagonally.
4. If the position is safe, place the queen and continue with the next column.
5. If all columns are filled, record the arrangement as a solution.
6. If no safe row exists in the current column, go back to the previous column and try the next possibility there.

This is the declarative layer of the seminar example: it explains what the algorithm should do before committing to the concrete Python structures and recursive calls used in the implementation.
