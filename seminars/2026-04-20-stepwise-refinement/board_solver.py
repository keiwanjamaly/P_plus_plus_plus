from copy import deepcopy
from typing import List, Tuple


class Board:
    def __init__(self, N: int = 8) -> None:
        self.positions: List[Tuple[int, int]] = []
        self.N = N

    def __str__(self) -> str:
        reset = "\033[0m"
        border = "\033[38;5;66m"
        label = "\033[38;5;214m"
        light_square = "\033[48;5;230m\033[38;5;236m"
        dark_square = "\033[48;5;65m\033[38;5;230m"
        queen = "\033[48;5;160m\033[38;5;230m\033[1m"

        separator = f"{border}  +" + "---+" * self.N + reset
        queen_positions = set(self.positions)
        lines = [separator]

        for row in range(self.N):
            squares = []
            for column in range(self.N):
                if (column, row) in queen_positions:
                    squares.append(f"{queen} Q {reset}")
                elif (column + row) % 2 == 0:
                    squares.append(f"{light_square}   {reset}")
                else:
                    squares.append(f"{dark_square} . {reset}")

            rank = self.N - row
            lines.append(
                f"{label}{rank:>2}{reset}{border}|{reset}"
                + f"{border}|{reset}".join(squares)
                + f"{border}|{reset}"
            )
            lines.append(separator)

        files = " ".join(f"{chr(ord('a') + column):^3}" for column in range(self.N))
        lines.append(f"{label}   {files}{reset}")
        return "\n".join(lines)


def add_queen(board: Board, column: int, row: int):
    board.positions.append((column, row))
    return board


def is_out_of_bounds(board: Board, column: int):
    return column >= board.N


def possible_rows(board: Board):
    all_occupied_rows = list(map(lambda pos: pos[1], board.positions))
    possible_rows_result: List[int] = []
    for row in range(board.N):
        if row not in all_occupied_rows:
            possible_rows_result.append(row)

    return possible_rows_result


def can_attack(queen_position: Tuple[int, int], column: int, row: int):
    column_difference = queen_position[0] - column
    row_difference = queen_position[1] - row
    return abs(column_difference) == abs(row_difference)


def safe_position(board: Board, column: int, row: int):
    for queen_position in board.positions:
        if can_attack(queen_position, column, row):
            return False

    return True


def add_queen_to_column(all_solutions: List[Board], board=None, column: int = 0):
    """Recursively place one queen per column, starting from an empty board."""
    if board is None:
        board = Board()

    if is_out_of_bounds(board, column):
        all_solutions.append(board)
    else:
        for row in possible_rows(board):
            if safe_position(board, column, row):
                new_board = add_queen(deepcopy(board), column, row)
                add_queen_to_column(all_solutions, new_board, column + 1)


def all_eight_queens():
    all_solutions = []
    add_queen_to_column(all_solutions)

    return all_solutions


def main():
    all_solutions = all_eight_queens()
    for board in all_solutions:
        print(board)
        print()

    print(len(all_solutions))


if __name__ == "__main__":
    main()
