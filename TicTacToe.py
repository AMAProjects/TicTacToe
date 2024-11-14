#Creating the board
board = [["  " for i in range(3)] for i in range(3)]


def print_board():
    print('__________')
    for row in board:
        print('|'+ '|'.join(row)+'|')
        print('|'+ ("__|" * 3))
        
print_board()
