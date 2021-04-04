import random

# Global variables used for random player start.
player = None
computer = None



# Board as dictionaries 

board ={1:" ",2:" ",3:" ",
        4:" ",5:" ",6:" ",
        7:" ",8:" ",9:" "}

# Random player start

def random_player():
    global player
    global computer
    '''Randomize starting player'''
    if random.randint(0,1) == 0:
        computer = "X"
        player = "O"
        print("Computer is first")
    else:
        player = "X"
        computer = "O"
        print("Player is first")

random_player()

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
    if board[1] == board[2] and board[1] == board[3] and board[1] == symbol:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == symbol):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == symbol):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == symbol):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == symbol):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == symbol):
        return True
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
    ''' Checks if position is empty and replaces it with letter and prints the board. 
        Tried to fix if symbol is placed on existing symbol but it does now work properly.
        So don't place symbol over existing symbol'''
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
    best_score = -800
    best_move = 0
    for key in board.keys():
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
    if (check_symbol_win(computer)):
        return 1
    elif (check_symbol_win(player)):
        return -1
    elif (check_draw()):
        return 0

    if (is_maximizing):
        best_score = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = computer
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > best_score):
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < best_score):
                    best_score = score
        return best_score
        


    if check_symbol_win(player):
        return -800

    elif check_symbol_win(computer):
        return 800

    elif check_draw():
        return 0
    
    if is_maximizing:
        best_score = -800

        for key in board.keys():
            if (board[key]) == " ":
                board[key] = computer
                score = minimax(board, 0, False)
                board[key] = " "
                if (score > best_score):
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, 0, True)
                board[key] = ' '
                if (score < best_score):
                    best_score = score
        return best_score

def restart_game():
    choice = input("Do you want to play again?(y/n) ")
    print()
    if choice == "y" or choice == "Y":
        global board
        board ={1:" ",2:" ",3:" ",
            4:" ",5:" ",6:" ",
            7:" ",8:" ",9:" "}
        random_player()
        print_board(board)
        check_win = False


while not check_win():
    ''' Switches players while game is not won'''
    if computer == "X":
        print("Computer's turn")
        computer_move()
        print("Player's turn")
        player_move()
    elif player == "X":
        print("Player's turn")
        player_move()
        print("Computer's turn")
        computer_move()


    
        

        
