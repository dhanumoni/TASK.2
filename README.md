#codsoft TASK.2
Tic-Tac-Toe AI program
🧩 1. Board Representation and Display
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


- The board is a 3×3 grid (list of lists).
- print_board() visualizes the game board in the console after every turn.

🏆 2. Checking for Winner
def check_winner(board):
    ...


- Checks if 'A' or 'B' has won.
- It evaluates:
- Rows: all(cell == player for cell in row)
- Columns: all(board[i][j] == player ...)
- Diagonals: both board[i][i] and board[i][2 - i]
- If all cells are filled and no one has won, returns "Draw".

🧮 3. Minimax Algorithm
def minimax(board, depth, is_maximizing):
    ...


- This is the heart of the AI logic.
- It recursively simulates all possible future moves:
- Maximizing player (AI 'B') chooses moves to maximize score.
- Minimizing player (Human 'X') chooses moves to minimize score.
- Scoring:
- 'B' win → +1
- 'A' win → –1
- Draw → 0

🎯 4. AI's Best Move Decision
def best_move(board):
    ...


- Runs through all available positions.
- Uses minimax() to find which move gives the best score for AI.
- Returns the row and column of that optimal move.

🎮 5. Main Game Loop
def play_game():
    ...


- The board is initialized with empty spaces.
- The game continues until someone wins or there's a draw.
- Human ('A') inputs a move.
- AI ('B') immediately responds with its move using best_move().

✨ Highlights
| Feature | Purpose | 
| Recursive AI logic | Makes AI unbeatable | 
| Player input | Allows interactive gameplay in console | 
| Dynamic evaluation | AI adjusts to real-time human decisions | 

