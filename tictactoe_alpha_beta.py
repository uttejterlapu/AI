import numpy as np

# Constants for players
PLAYER_X = 1
PLAYER_O = -1
EMPTY = 0

def create_board():
    # Create an empty 3x3 game board
    return np.zeros((3, 3), dtype=int)

def is_winner(board, player):
    # Check if the player has won
    for i in range(3):
        if np.all(board[i, :] == player) or np.all(board[:, i] == player):
            return True
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

def is_draw(board):
    # Check if the game is a draw
    return not (EMPTY in board)

def game_over(board):
    # Check if the game is over (win or draw)
    return is_winner(board, PLAYER_X) or is_winner(board, PLAYER_O) or is_draw(board)

def available_moves(board):
    # Get a list of available moves (empty cells)
    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == EMPTY]

def minimax(board, depth, maximizing_player):
    if is_winner(board, PLAYER_X):
        return 1
    if is_winner(board, PLAYER_O):
        return -1
    if is_draw(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in available_moves(board):
            board[move] = PLAYER_X
            eval = minimax(board, depth + 1, False)
            board[move] = EMPTY
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in available_moves(board):
            board[move] = PLAYER_O
            eval = minimax(board, depth + 1, True)
            board[move] = EMPTY
            min_eval = min(min_eval, eval)
        return min_eval

def alpha_beta_pruning(board):
    best_move = None
    alpha = float('-inf')
    beta = float('inf')
    max_eval = float('-inf')

    for move in available_moves(board):
        board[move] = PLAYER_X
        eval = minimax(board, 0, False)
        board[move] = EMPTY

        if eval > max_eval:
            max_eval = eval
            best_move = move

        alpha = max(alpha, eval)
        if alpha >= beta:
            break

    return best_move

def print_board(board):
    for row in board:
        print(" ".join(["X" if cell == PLAYER_X else "O" if cell == PLAYER_O else "-" for cell in row]))

def main():
    board = create_board()
    print("Tic-Tac-Toe Game:")
    print_board(board)

    while not game_over(board):
        player_move = tuple(map(int, input("Enter your move (row col): ").split()))
        if board[player_move] != EMPTY:
            print("Invalid move. Try again.")
            continue
        board[player_move] = PLAYER_O
        print_board(board)

        if not game_over(board):
            print("Computer is thinking...")
            computer_move = alpha_beta_pruning(board)
            board[computer_move] = PLAYER_X
            print_board(board)

    if is_winner(board, PLAYER_X):
        print("Computer wins!")
    elif is_winner(board, PLAYER_O):
        print("You win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
