import random

# Global variables used for random player start.
player = None
computer = None

# Lists with available input options

available_moves = ["1","2","3","4","5","6","7","8","9"]
available_choices = ["y","Y","n","N"]

# Empty board as dictionary with keys 

board ={1:" ",2:" ",3:" ",
        4:" ",5:" ",6:" ",
        7:" ",8:" ",9:" "}

# Random player start

def random_player():
    ''' Overwrites global variables '''
    global player
    global computer
    '''Randomize starting player using python random'''
    if random.randint(0,1) == 0:
        computer = "X"
        player = "O"
    else:
        player = "X"
        computer = "O"

random_player()


def print_board(board):
    ''' Prints visual board in terminal. Available moves was planned to replace index with empty 
        position but could not make it work for computer moves.'''
    print("\033c", end="")
    print()
    print(" " + board[1] + " | " + board[2] + " | " + board[3] + "     " + available_moves[0] + " | " + available_moves[1] + " | " + available_moves[2])
    print("---+---+---")
    print(" " + board[4] + " | " + board[5] + " | " + board[6] + "     " + available_moves[3] + " | " + available_moves[4] + " | " + available_moves[5])
    print("---+---+---")
    print(" " + board[7] + " | " + board[8] + " | " + board[9] + "     " + available_moves[6] + " | " + available_moves[7] + " | " + available_moves[8])
    print()

print_board(board)

def position_is_free(position):
    ''' Checks if position is empty and returns boolean value'''
    if (board[position] == " "):
        return True
    else: 
        return False

def check_win():
    ''' checks rows, columns and diagonals for matching symbols and returns boolean '''
    # Checks rows
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    # Check columns
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    # Check diagonals
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def check_symbol_win(symbol):
    ''' Checks board for minimax algorithm '''
    # Checks rows
    if board[1] == board[2] and board[1] == board[3] and board[1] == symbol:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == symbol):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == symbol):
        return True
    # Check columns
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == symbol):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == symbol):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == symbol):
        return True
    # Check diagonals
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == symbol):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == symbol):
        return True
    else:
        return False



def check_draw():
    ''' Checks positions on board. If there is no free spaces returns draw '''
    for key in board.keys():
        if (board[key] == ' '):
            return False
    return True

def insert_letter(letter,position):
    ''' Checks if position is empty and replaces it with letter and prints the board '''
    if position_is_free(position):
        board[position] = letter
        print_board(board)
        if (check_win()):
            if letter == computer:
                print("Computer wins!")
                restart_game()
            elif letter == player:
                print("Player wins!")
                restart_game()
            return
        
        if(check_draw()):
            print("Draw!")
            restart_game()
    else:
        print("Invalid position")
        ''' if invalid position following code repeats until correct position is entered '''
        input(int("Input new position: "))
        insert_letter(letter,position)

def player_move():
    ''' Fixes wrong input for player '''
    while True:
        try:  
            position = input("Enter position for " + player + ": ")
            position = int(position)
            insert_letter(player,position)
            return
        except KeyError:
            continue
        except ValueError:
            continue
        else:
            break

def computer_move():
    ''' Starting values for initialization '''
    best_score = -500
    best_move = 0
    for key in board.keys():
        ''' Maximiser goes thru all moves to find best move for using minimax algorithm '''
        if (board[key] == ' '):
            board[key] = computer
            score = minimax(board, 0, False)
            board[key] = ' '
            if (score > best_score):
                best_score = score
                best_move = key

    insert_letter(computer, best_move)
    return


def minimax(board, depth, is_maximizing):
    ''' Adds value on simulated turns 1 for computer win, 0 for draw and -1 for player win'''
    if (check_symbol_win(computer)):
        return 1
    elif (check_symbol_win(player)):
        return -1
    elif (check_draw()):
        return 0

    if (is_maximizing):
        ''' Maximizer '''
        best_score = -500
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = computer
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > best_score):
                    best_score = score
        return best_score

    else:
        ''' Minimizer '''
        best_score = 500
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < best_score):
                    best_score = score
        return best_score
        


    if check_symbol_win(player):
        return -500

    elif check_symbol_win(computer):
        return 500

    elif check_draw():
        return 0
    
    if is_maximizing:
        ''' This part finds best score for each possible position until it reaches terminal state'''
        best_score = -500

        for key in board.keys():
            if (board[key]) == " ":
                board[key] = computer
                score = minimax(board, 0, False)
                board[key] = " "
                if (score > best_score):
                    best_score = score
        return best_score

    else:
        best_score = 500
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, 0, True)
                board[key] = ' '
                if (score < best_score):
                    best_score = score
        return best_score

def restart_game():
    ''' restart game function sometimes does not work properly.
        When it does work properly overwrites global variables and prints clean game board'''
    print()
    choice = input("Do you want to play again?(y/n) ")
    print()
    if choice == "y" or choice == "Y":
        global board
        global player
        global computer
        board ={1:" ",2:" ",3:" ",
            4:" ",5:" ",6:" ",
            7:" ",8:" ",9:" "}
        random_player()
        print_board(board)
        while not check_win():
            ''' Switches players while game is not won'''
            if computer == "X":
                print("Computer's turn")
                print()
                computer_move()
                print("Player's turn")
                print()
                player_move()
            elif player == "X":
                print("Player's turn")
                print()
                player_move()
                print("Computer's turn")
                print()
                computer_move()
    elif choice == "n" or choice == "N":
        exit()
    while choice not in available_choices:
        ''' If wrong input was entered program stops working so I had to repeat'''
        choice = input("Do you want to play again?(y/n) ")
        print()
        if choice == "y" or choice == "Y":
            board ={1:" ",2:" ",3:" ",
                4:" ",5:" ",6:" ",
                7:" ",8:" ",9:" "}
            random_player()
            print_board(board)
        elif choice == "n" or choice == "N":
            exit()


while not check_win():
    ''' Switches players while game is not won'''
    if computer == "X":
        print("Computer's turn")
        print()
        computer_move()
        print("Player's turn")
        print()
        player_move()
    elif player == "X":
        print("Player's turn")
        print()
        player_move()
        print("Computer's turn")
        print()
        computer_move()