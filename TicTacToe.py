# Creating the board
board = [["  " for _ in range(3)] for _ in range(3)]

def print_board():
    print('__________')
    for row in board:
        print('|'+ '|'.join(row)+'|')
        print('|'+ ("__|" * 3))

print_board()

# Player Alternation
current_player = 'X'

def play_position(row, column, current_player):
    if 0 <= row < 3 and 0 <= column < 3 and board[row][column] == "  ":
        board[row][column] = current_player + " "
        print_board()
    else:
        print('Oops, this spot is already taken or the input is out of bounds! Try a different one.')
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        column = int(input("Enter column (0, 1, or 2): "))
        play_position(row, column, current_player)

def check_winner(current_player):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == current_player + " ":
            return True
    # Check columns
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == current_player + " ":
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == current_player + " " or \
       board[0][2] == board[1][1] == board[2][0] == current_player + " ":
        return True
    return False

def check_tie():
    for row in board:
        if "  " in row:
            return False
    return True

def game_loop():
    global current_player
    while True:
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        column = int(input("Enter column (0, 1, or 2): "))
        play_position(row, column, current_player)
        if check_winner(current_player):
            print(f'Player {current_player} won the game!!')
            break
        elif check_tie():
            print("Game Over, it's a tie!")
            break
        else:
            current_player = 'O' if current_player == 'X' else 'X'

game_loop()