# Board as dictionaries 

board ={1:" ",2:" ",3:" ",
        4:" ",5:" ",6:" ",
        7:" ",8:" ",9:" "}

def print_board(board):
    ''' Prints visual board in terminal'''
    print()
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "     1 | 2 | 3")
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "     4 | 5 | 6")
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "     7 | 8 | 9")
    print()

print_board(board)

def position_is_free(position):
    ''' Checks if position is empty and returns boolean value'''
    if (board[position] == " "):
        return True
    else: 
        return False

def check_win():
    pass

def check_draw():
    ''' Checks positions on board. If there is no free spaces returns draw'''
    for key in board.keys():
        if board[key] == " ":
            return False
        return True

def insert_letter(letter,position):
    ''' Checks if position is empty and replaces it with letter and prints the board'''
    if position_is_free(position):
        board[position] = letter
        print_board(board)
        if (check_win()):
            return
        
        if(check_draw()):
            return
    else:
        print("Invalid position")
        input(int("Input new position: "))
        insert_letter(letter,position)
        return