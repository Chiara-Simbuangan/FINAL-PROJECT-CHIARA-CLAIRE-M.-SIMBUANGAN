def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, mark):
    """Checks if there is a winner."""
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == mark for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2 - i] == mark for i in range(3)):
        return True
    return False

def is_draw(board):
    """Checks if the game is a draw."""
    return all(all(cell != " " for cell in row) for row in board)

def get_move(player_name):
    """Gets the player's move."""
    while True:
        try:
            row = int(input(f"{player_name}, enter the row (1, 2, or 3): ")) - 1
            col = int(input(f"{player_name}, enter the column (1, 2, or 3): ")) - 1
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")

def main():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Get player names
    player1 = input("Enter the name of Player 1: ")
    player2 = input("Enter the name of Player 2: ")
    players = [(player1, "X"), (player2, "O")]
    
    current_player = 0
    
    # Game loop
    while True:
        print_board(board)
        player_name, mark = players[current_player]
        print(f"{player_name}'s turn. You are '{mark}'.")
        
        while True:
            row, col = get_move(player_name)
            if board[row][col] == " ":
                board[row][col] = mark
                break
            else:
                print("Cell already taken. Choose a different cell.")
        
        if check_winner(board, mark):
            print_board(board)
            print(f"Congratulations {player_name}, you win!")
            break
        elif is_draw(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = 1 - current_player

if __name__ == "__main__":
    main()
