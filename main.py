def all_8_queens():
    x = [0] * 9
    rows = [True] * 9
    diag1 = [True] * 17
    diag2 = {k: True for k in range(-7, 8)}
    solutions = []

    def safe(i, j):
        return rows[i] and diag1[i + j] and diag2[i - j]

    def set_queen(i, j):
        rows[i] = False
        diag1[i + j] = False
        diag2[i - j] = False
        x[j] = i

    def remove_queen(i, j):
        rows[i] = True
        diag1[i + j] = True
        diag2[i - j] = True

    def try_column(j):
        for i in range(1, 9):
            if safe(i, j):
                set_queen(i, j)

                if j == 8:
                    solutions.append(x[1:].copy())
                else:
                    try_column(j + 1)

                remove_queen(i, j)

    try_column(1)
    return solutions

if __name__ == "__main__":
    print(all_8_queens())
