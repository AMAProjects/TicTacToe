#Creating the board
board = [["  " for i in range(3)] for i in range(3)]


def print_board():
    print('__________')
    for row in board:
        print('|'+ '|'.join(row)+'|')
        print('|'+ ("__|" * 3))
        
print_board()

#Player Alternation
current_player = 'X'

#Rows and columns input
row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
column = int(input("Enter column (0, 1, or 2): "))


#Changing board from player input
def play_position(row, column, current_player):
    if board[row][column] == "  ":
        board[row][column] = current_player + " " 
    else:
        print('Oops, this spot is already taken! Try a different one.')
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        column = int(input("Enter column (0, 1, or 2): "))
        board[row][column] = current_player + " " 
    
        
play_position(row, column, current_player)
print_board()

#Check for winner
def line_wins(line, current_player):
    return line[0]==line[1]==line[2] == current_player

def check_winner(current_player):
    #Checking rows
    for row in range(3):
        if line_wins(board[row], current_player):
            print(f'Player {current_player} won the game!!')
            return True
    #Checking columns
    for column in range(3):
        if line_wins(board[column], current_player):
            print(f'Player {current_player} won the game!!')
            return True
    #Checking diagonals
    diagonals = [board[0][0], board[1][1], board[2][2]], [board[0][2], board[1][1], board[2][0]]
    for diagonal in diagonals:
        if line_wins(diagonal,current_player):
            print(f'Player {current_player} won the game!!')
            return True
    return False
    
#Keeping the game's loop
end_game = False

while not end_game:
    if check_winner(current_player):  # Check for a winner
        end_game = True 
        print("Game Over.") # End the game if there is a winner
    else:
        # Switch player after each valid turn
        current_player = 'O' if current_player == 'X' else 'X'
        row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
        column = int(input("Enter column (0, 1, or 2): "))
        play_position(row, column, current_player)
        print_board()  # Update board