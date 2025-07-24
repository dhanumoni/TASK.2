import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for player in ['A', 'B']:
        # Check rows, columns, and diagonals
        win = any(
            all(cell == player for cell in row) or
            all(board[i][j] == player for i in range(3)) for j, row in enumerate(board)
        ) or all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3))
        if win:
            return player
    if all(cell in ['A', 'B'] for row in board for cell in row):
        return "Draw"
    return None

def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result == 'B': return 1
    if result == 'A': return -1
    if result == 'Draw': return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'B'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'A'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    move = None
    best_score = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'B'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print("Winner:", winner)
            break
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter col (0-2): "))
        if board[row][col] == ' ':
            board[row][col] = 'A'
            if not check_winner(board):
                ai_row, ai_col = best_move(board)
                board[ai_row][ai_col] = 'B'
        else:
            print("Invalid move! Try again.")

play_game()
