#  Made By Aniket Batabyal @anarchymonkey
#  Took help from  Udemy as part of the Python devoloper Bootcamp course
#   All codes are made with Python 3.6x
#   For furthur info contact me on github      LINK :  https://github.com/anarchymonkey


import typing
import string
import random


#  made the board with simple listing of data
def make_play_board(board):
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


test_board = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O']  # these are the markers set for testing


#  Asking if the player wants to be X or an O , Baiscally selecting Player 1 for the game

def ask_XO():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = ''
        play = input('What do you wanna be X or O').upper()

        if marker == 'X':
            return 'X', 'O'
        else:
            return 'O', 'X'


#  Placing the marker if you are unsure of your position


def board_position_marker(board, marker, position):
    board[position] = marker


#  Now Checking function  For the Winner

def winner_winner_chicken_dinner(board, mark):
    return ((board[9] == mark and board[8] == mark and board[7] == mark)  # upper straight
            or (board[7] == mark and board[4] == mark and board[1] == mark)  # lower left straight down
            or (board[7] == mark and board[5] == mark and board[3] == mark)  # digonal
            or (board[8] == mark and board[5] == mark and board[2] == mark)
            or (board[9] == mark and board[6] == mark and board[3] == mark)
            or (board[9] == mark and board[5] == mark and board[1] == mark)
            or (board[4] == mark and board[5] == mark and board[6] == mark)
            or (board[1] == mark and board[2] == mark and board[3] == mark))


#  selecting Random winners

def choose_first():
    pass
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


#  check if the space is freely avialable or not

def space_check(board, pos):
    return board[pos] == ' '


#  checks if the board is full or not

def check_board_full(board):
    for i in range(1, 10):

        if space_check(board, i):
            return False
        else:
            return True


#  now for the player choices

def players_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] or not space_check(board, position):
        position = int(input('Please Enter your choice for the next pos (1-9)'))

    return position


def replay():
    return input('Do you want to play again sir? Enter Yes or no').lower().startswith('y')


print('WELCOME SIRRRRR TO TICCC TACCCC TOEEEEEEEE')

while True:
    pass
    # Reset the board

    test_board = [' '] * 10  # made the board empty
    player1_marker, player2_marker = ask_XO()  # ask which markers does the players want X or O

    turn = choose_first()  # turn will be decided for Player 1 or 2

    print(turn + 'Will Go First! ALL THE BEST')

    play_game = input('Are you ready to play??????,Enter YES or NO')

    if play_game.lower() == 'y':

        game_on = True
    else:
        game_on = False

    while game_on:

        #  will go untill there is a winner

        if turn == 'Player 1':

            #  Player ones turn

            make_play_board(test_board)
            position = players_choice(test_board)
            board_position_marker(test_board, player1_marker, position)  # set the X position

            if (winner_winner_chicken_dinner(test_board, position)):  # if player 1 is the winner
                check_board_full(test_board)  # check if the board is full
                make_play_board(test_board)  # display the board
                print('Congrats You Have won the game')
                game_on = False  # return to yes no screen

            else:  # it will be a draw
                if check_board_full(test_board):
                    make_play_board(test_board)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 2'

        else:

            # this is for player 2 to first make the board and place the position
            make_play_board(test_board)
            position = players_choice(test_board)
            board_position_marker(test_board, player2_marker, position)  # board[position]==marker which is X or Y

            if winner_winner_chicken_dinner(test_board,
                                            player2_marker):  # if player 2 wins, this function checks for the winners
                make_play_board(test_board)
                print('PLAYER 2 IS THE WINNER  ')
                game_on = False  # End

            else:
                if check_board_full(test_board):  # check if the board is full or not
                    make_play_board(test_board)
                    print('The game is a draw')  # game is draw
                    break
                else:
                    turn = 'Player 1'  # return back to player 1's turn
    if not replay():  # if the player says no then break
        break
