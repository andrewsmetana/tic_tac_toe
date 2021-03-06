# Simple Tic Tac Toe Game
# Andrew Smetana
# 11/9/2020

# -----Global Variables--------

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
play_new_game = True
game_still_going = True
winner = "None"
current_player = 'X'

# --------------------------------------------

def play_game():
    # Used to determine if they user wants to keep playing after finishing a game
    while play_new_game:

        display_board()

        # Used to run through game sequence until win or tie is identified
        while game_still_going:

            handle_turn(current_player)

            check_if_game_over()

            flip_player()

        # The Game is Over. Win or Tie.
        global winner
        if winner == "None":
            print("Game ended in a Tie")
        else:
            print("Player " + winner + " won the game!")
            #Play again?
            play_new_game()


def display_board():
    # Displays board in 3x3 layout
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn(player):
    position = input("Player " + player + ". Choose a position from 1-9: ")

    # Input Validation
    valid = False
    while not valid:
        # Check to see if input is a # between 1 and 9
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid entry. Player " + player + ". Choose a position from 1-9: ")

        # Player enters 1-9, translate to table 0-8
        position = int(position) - 1

        # Check to see if that space has already been played.
        if board[int(position)] in ["X", "O"]:
            valid = False
            position = input("That space is taken. Player " + player + ". Choose a position from 1-9: ")
        else:
            valid = True

    board[position] = player
    display_board()


def check_if_game_over():
    # After every entry, game checks for 3 in a row of the same symbol
    check_for_winner()
    check_for_tie()


def check_for_winner():
    global game_still_going
    global winner
    global current_player
    # Column win check
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"

    # Rows win check
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    # Diagonals win check
    TLtoBR = board[0] == board[4] == board[8] != "-"
    BLtoTR = board[6] == board[4] == board[2] != "-"

    # If any conditions are met, update game_still_going parameter
    if column1 or column2 or column3 or row1 or row2 or row3 or TLtoBR or BLtoTR:
        game_still_going = False
        winner = current_player


def check_for_tie():
    global game_still_going
    # Checks to see if any blank spaces remain on board
    if "-" not in board:
        game_still_going = False


def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'


def play_new_game():
    global play_new_game
    # After game is over, ask if they would like to play again
    cont = input("Type 1 to play again. Type anything else to quit.")
    if cont != "1":
        play_new_game = False
    else:
        reset_board()


def reset_board():
    global board
    global game_still_going
    global winner
    global current_player
    # If they want to play again, reset board
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    game_still_going = True
    winner = "None"
    current_player = 'X'


# ------MAIN--------

play_game()
