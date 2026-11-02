#  Implement Backtracking search to solve the 8-Queens constraint satisfaction problem

N = 8
board = [-1] * N

def safe(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == row - i:
            return False
    return True

def solve(row):
    if row == N:
        return True

    for col in range(N):
        if safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False

solve(0)

for row in range(N):
    for col in range(N):
        print("Q" if board[row] == col else ".", end=" ")
    print()