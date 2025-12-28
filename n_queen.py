def read_input(filename):
    with open(filename, "r") as file:
        n = int(file.readline().strip())
    return n


def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_n_queen(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queen(board, row + 1, n):
                return True
            board[row][col] = 0  # Backtracking

    return False


def n_queen(n):
    board = [[0] * n for _ in range(n)]

    if solve_n_queen(board, 0, n):
        return True, board
    return False, []


# -------- MAIN --------
filename = "input_n_queen.txt"
n = read_input(filename)

possible, solution = n_queen(n)

if possible:
    print("Solution exists:")
    for row in solution:
        print(row)
else:
    print("No solution exists")
