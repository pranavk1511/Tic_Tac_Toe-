import os

# Initialize the game board
board = [' ' for _ in range(9)]

# Helper function to print the game board
def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# Helper function to check if a player has won
def check_win(player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True

    # No winner yet
    return False

# Helper function to check if the board is full
def check_full():
    return ' ' not in board

# Main game loop
def play_game():
    current_player = 'X'
    while True:
        print_board()

        # Get the current player's move
        move = int(input(f"{current_player}'s turn (0-8): "))

        # Check if the move is valid
        if board[move] == ' ':
            board[move] = current_player

            # Check if the current player has won
            if check_win(current_player):
                print_board()
                print(f"{current_player} wins!")
                break

            # Check if the game is a tie
            if check_full():
                print_board()
                print("It's a tie!")
                break

            # Switch to the other player
            current_player = 'O' if current_player == 'X' else 'X'

        else:
            print("Invalid move, try again.")

        # Clear the screen for a better user experience
        os.system('cls' if os.name == 'nt' else 'clear')

# Start the game
play_game()