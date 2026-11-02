#  Develop a game-playing agent using the Minimax algorithm for optimal decision-making.

def minimax(board, is_max):
    if "X" in board and check(board, "X"):
        return -1
    if "O" in board and check(board, "O"):
        return 1
    if " " not in board:
        return 0

    scores = []
    
    for i in range(9):
        if board[i] == " ":
            board[i] = "O" if is_max else "X"
            scores.append(minimax(board, not is_max))
            board[i] = " "
    return (max if is_max else min)(scores)

def check(b, p):
    return any(all(b[i] == p for i in line) for line in
        [(0,1,2),(3,4,5),(6,7,8),(0,3,6),
         (1,4,7),(2,5,8),(0,4,8),(2,4,6)])

board = [" "] * 9

while True:
    print("\n", board[:3], "\n", board[3:6], "\n", board[6:])
    move = int(input("Your move (0-8): "))
    if move not in range(9) or board[move] != " ":
        print("Invalid move!")
        continue
    board[move] = "X"

    if check(board, "X"):
        print("You win!")
        break
    if " " not in board:
        print("Draw!")
        break

    best, score = -1, -2
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            s = minimax(board, False)
            board[i] = " "
            if s > score:
                best, score = i, s
    board[best] = "O"

    if check(board, "O"):
        print("AI wins!")
        break
    if " " not in board:
        print("Draw!")
        break

