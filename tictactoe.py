import random
from os import system

# Board

board = [" "," "," "," "," "," "," "," "," "]

# Active game. Game is going while this is true

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


# Display board

def display_board():
    '''Displays list as game board'''
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print()
    print("Available moves:")
    print(available_moves)

def check_rows():
    ''' Checks if rows match'''
    global active_game
    row_1 = board[0] == board[1] == board[2] != " "
    row_2 = board[3] == board[4] == board[5] != " "
    row_3 = board[6] == board[7] == board[8] != " "
    if row_1 or row_2 or row_3:
        ''' If rows match game stops'''
        active_game = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]        
    return

def check_columns():
    ''' Checks if columns match'''
    global active_game
    column_1 = board[0] == board[3] == board[6] != " "
    column_2 = board[1] == board[4] == board[7] != " "
    column_3 = board[2] == board[5] == board[8] != " "
    if column_1 or column_2 or column_3:
        ''' If columns match game stops'''
        active_game = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]    
    return

def check_diagonals():
    global active_game
    ''' Checks if diagonals match'''
    diagonal_1 = board[0] == board[4] == board[8] != " "
    diagonal_2 = board[2] == board[4] == board[6] != " "
    if diagonal_1 or diagonal_2:
        ''' If diagonals match game stops'''
        active_game = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]
    return


def check_win():
    ''' Checks if board positions match '''
    global winner
    row_win = check_rows()
    column_win = check_columns()
    diagonal_win = check_diagonals()
    if row_win:
        winner = row_win
    elif column_win:
        winner = column_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None


def check_tie():
    ''' If all fields are full game stops'''
    global active_game
    if " " not in board and winner == None:
        active_game = False
        print("Tie!")
    return

def switch_player():
    global current_player
    ''' switches player every turn'''
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return

def game():
    '''Main function for gameplay'''
    display_board()
    
    while active_game:
        game_turn(current_player)
        check_win()
        check_tie()
        switch_player()

    if winner == "X" or winner == "O":
        print(winner + " won!")
    elif winner == None:
        return

def game_turn(player):
    global count
    global available_moves
    print(player + "'s turn.")
    position = input("Enter position from 1 to 9: ")

    if position not in available_moves:
        position = input("Invalid position. Enter position from 1 to 9: ")
    ''' There must be easier way to do this. '''
    if position == "1":
        available_moves.remove("1")
    elif position == "2":
        available_moves.remove("2")
    elif position == "3":
        available_moves.remove("3")
    elif position == "4":
        available_moves.remove("4")
    elif position == "5":
        available_moves.remove("5")
    elif position == "6":
        available_moves.remove("6")
    elif position == "7":
        available_moves.remove("7")
    elif position == "8":
        available_moves.remove("8")
    elif position == "9":
        available_moves.remove("9")
    '''fixes input so it matches board indexes'''
    position = int(position) -1
    board[position] = player
    count += 1
    print("Turn " + str(count))
    display_board()
    

game()



