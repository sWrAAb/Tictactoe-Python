# Board as dictionaries 

board ={1:" ",2:" ",3:" ",
        4:" ",5:" ",6:" ",
        7:" ",8:" ",9:" "}

def print_board(board):
    print()
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "     1 | 2 | 3")
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "     4 | 5 | 6")
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "     7 | 8 | 9")
    print()

print_board(board)