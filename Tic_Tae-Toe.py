# Workflow
# 1. Create the board
# 2. Display the board
# 3. Get the player's move
# 4. Check for a win or a tie
# 5. Switch players
# 6. Repeat steps 2-5 until the game is over
# Create the board
board = [" " for _ in range(9)]
# Display the board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
# Get the player's move
def get_player_move(player):
    move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    while board[move] != " ":
        print("That spot is already taken. Try again.")
        move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
    board[move] = player
# Check for a win or a tie
def check_win(player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def check_tie():
    return all(space != " " for space in board)
# Main game loop
def main():
    current_player = "X"
    while True:
        display_board()
        get_player_move(current_player)
        if check_win(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break
        if check_tie():
            display_board()
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"
if __name__ == "__main__":
    main()
    