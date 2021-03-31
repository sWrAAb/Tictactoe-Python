import random
from os import system

# Board

board = [" "," "," "," "," "," "," "," "," "]

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

# Display board

def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()

display_board()


available_moves = ["1","2","3","4","5","6","7","8","9"]
print("Available moves:")
print(available_moves)

def game():
    game_turn()

def game_turn():
    position = input("Enter position: ")
    position = int(position) -1

    board[position] = "X"
    display_board()

game()
