def print_board():
    ''' Prints board with numbers'''
    board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
    for row in board:
        print("| " + " |".join(row) +' |' )

print_board()