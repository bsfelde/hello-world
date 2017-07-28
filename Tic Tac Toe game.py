from __future__ import print_function 

import random

import os


def display_board(board):
    
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

def player_input():
	#asks if they want to be Xs or Os

    marker = ''
    #set marker before, so while not loop fires
    while not (marker == 'O' or marker == 'X'):
        #.upper to take in either lowercase or upper
        marker = raw_input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
	#sets where the player went
    #assigning index on board to marker
    board[position] = marker

def win_check(board,mark):
    #checks if mark is each of these three positions
    #if so, that player has won
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
	

def choose_first():
    dice = random.randint(1,7)
    print('Rolling dice...')

    if dice%2 == 0:
        print(str(dice) + ("\nIt's EVEN, so Player 1 goes first!"))
        return 'Player 1'
    else:
        print(str(dice) + ("\nIt's ODD, so Player 2 goes first!"))
        return 'Player 2'


def space_check(board, position):
	#checks to see if one of the board positions is empty
    return board[position] == ' '

def full_board_check(board):
	#checks to see if the board is full or not
    for i in range(1,10):
        #if the above, board at position i, is a space
        #return false, because it's not full yet
        if space_check(board, i):
            return False
    return True 

def player_choice(board):
	#asks where the player wants to go and puts it there
    position = ' '
    #continually ask until valid aka until space is full
    #.split() replaces empty spaces in string, returns them as a list
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = raw_input('Choose your next position: (1-9) ')
    return int(position)

def replay():
	#asks if they want to replay
    #lower case-ing the input
    #return true for yea, yes, yup, etc
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#=====================================================================================

print('Welcome to Tic Tac Toe!')

while True:
	#continually run the game until something goes false
	theboard = [' ']*10
	player1_marker, player2_marker = player_input()
	turn = choose_first()
	print (turn + '!')

	game_on = True

	while game_on:
		if turn == 'Player 1':

			display_board(theboard)
			#show board
			position = player_choice(theboard)
			#ask where the player wants to go
			place_marker(theboard, player1_marker, position)
			#put Player 1's marker at that position, on the board

			if win_check(theboard, player1_marker):
				#see if Player 1's marker has returned True for win_check
				display_board(theboard)
				print('Congrats, Player 1, You have won!')
				game_on = False
			else:
				if full_board_check(theboard):
					#check to see if the board is full aka a tie
					display_board(theboard)
					print('The game is a draw!')
					break
				else:
					turn = 'Player 2'
		else:
			display_board(theboard)
			position = player_choice(theboard)
			place_marker(theboard, player2_marker, position)

			if win_check(theboard, player2_marker):
				display_board(theboard)
				print('Congrats, Player 2, You have won!')
				game_on = False
			else:
				if full_board_check(theboard):
					display_board(theboard)
					print('The game is a tie!')
					break
				else:
					turn = 'Player 1'

	if not replay():
		break 

