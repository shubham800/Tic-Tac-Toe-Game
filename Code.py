import random
def display_board(boards):
    print('  |   |')
    print('' + boards[7] + ' | ' + '' + boards[8] + ' | ' + '' + boards[9])
    print('  |   |')
    print('---------')
    print('  |   |')
    print('' + boards[4] + ' | ' + '' + boards[5] + ' | ' + '' + boards[6])
    print('  |   |')
    print('---------')
    print('  |   |')
    print('' + boards[1] + ' | ' + '' + boards[2] + ' | ' + '' + boards[3])
    print('  |   |')

def user_inpurt():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input("Player1: Do you want X or O> ").upper()

    if marker == 'x':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in (1,2,3,4,5,6,7,8,9) or not space_check(board, position):
        position = int(input("Choose your postion (1-9)> "))

    return position

def replay():
    return input("Do you want to play again Yes or No> ").lower().startswith('y')

print("Welcome to the Tic-Tac-Toe!".center(100))
while True:
    theboard = [' '] * 10
    player1_marker, player2_marker = user_inpurt()
    turn = choose_first()
    print(f"{turn} will go first.")

    play_game = input("Are you ready to play? Enter Yes or No> ")
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':

            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player1_marker, position)

            if win_check(theboard, player1_marker):
                display_board(theboard)
                print("Congratulation! You have won the game.")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("Ohh! The game has draw.")
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, player2_marker, position)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print("Player 2 has won.")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("Ohh! The game has draw.")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
