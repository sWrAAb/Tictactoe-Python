import random
from os import system

# Board

board = [" "," "," "," "," "," "," "," "," "]

# Active game

active_game = True
count = 0

# Winner

winner = None

# Current player

current_player = "X"

# Random player

def random_player():
    '''Randomize starting player'''
    if random.randint(0,1) == 0:
        print("Computer is first")
        return "Computer"
    else:
        print("Player is first")
        return "Player"

random_player()

# Avaliable moves

available_moves = ["1","2","3","4","5","6","7","8","9"]
print("Available moves:")

# Display board

def display_board():
    '''Displays list as game board'''
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()
    print(available_moves)

def check_rows():
    ''' Checks if rows match'''
    global active_game
    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "
    return

def check_columns():
    ''' Checks if columns match'''
    global active_game
    column_1 = board[0] == board[3] == board[6] != " "
    column_2 = board[1] == board[4] == board[7] != " "
    column_3 = board[2] == board[5] == board[8] != " "
    return

def check_diagonals():
    global active_game
    ''' Checks if diagonals match'''
    diagonal_1 = board[0] == board[4] == board[8] != " "
    diagonal_2 = board[2] == board[4] == board[6] != " "
    return


def check_win():
    ''' Checks if board positions match '''
    check_rows()
    check_columns()
    check_diagonals()


def check_tie():
    return

def switch_player():
    return

def game():
    '''Main function for gameplay'''
    display_board()
    
    while active_game:
        game_turn()
        check_win()
        check_tie()
        switch_player()

    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        print("Tie!")

def game_turn():
    global count
    position = input("Enter position: ")
    position = int(position) -1
    count += 1
    print(available_moves)
    board[position] = "X"
    display_board()
    print(count)
    

game()

