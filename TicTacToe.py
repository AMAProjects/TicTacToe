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

#Rows and collumns input
row = int(input("Enter row (0, 1, or 2): "))
column = int(input("Enter column (0, 1, or 2): "))


