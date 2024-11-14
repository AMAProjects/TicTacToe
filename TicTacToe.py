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
if current_player == 'X':
    current_player = 'O'
else:
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
    
        
play_position(row,column, current_player)
print_board()

#Check for winner
def line_wins(line, current_player):
    return line[0]==line[1]==line[2] == current_player

def check_winner(row, column, current_player):
      for row in range(3):
        if line_wins(board[row], current_player):
            print(f'Player {current_player} won the game!!')
            return True
        