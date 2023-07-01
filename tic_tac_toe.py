# here i would follow some of the steps from the book to recreate a 
# tic-tac-toe game lets see how it comes out

# step-one list out the major processes to be done in seperate steps 
# step-two would be writing out the codes, and execution
# step-three would be continious modification and editing of the codes.


# 1 list out major steps

# - make a ditionary containing the locations on the tic tac toe board
# - write a func thats converts those steps into a visual representation for
# players to see
# - now implement that func inside a for loop that allows players to take 
# turns playing and ends when the it has been looped through 4 times or when 
# a player wins

# 2 write out the code

game_board = {'TL' : ' ', 'TM' : ' ', 'TR' : ' ',
              'ML' : ' ', 'MM' : ' ', 'MR' : ' ',
              'BL' : ' ', 'BM' : ' ', 'BR' : ' '}

def TTT():
    print(game_board['TL'] + ' | ' + game_board['TM'] + ' | ' + game_board['TR'])
    print(game_board['ML'] + ' | ' + game_board['MM'] + ' | ' + game_board['MR'])
    print(game_board['BL'] + ' | ' + game_board['BM'] + ' | ' + game_board['BR']) 

def board_0():
    print('TL' + ' | ' + 'TM' + ' | ' + 'TR') ,
    print('ML' + ' | ' + 'MM' + ' | ' + 'MR') ,
    print('BL' + ' | ' + 'BM' + ' | ' + 'BR' + '\n') ,
    print('this represent places on the board '  + '\n'),
    print('so you use them to pick a position to move'  + '\n'),
    print('e.g TL = top_left, BR = bottom_right' + '\n'),
    print('you get the idea now right' + '\n')

def game_TTT():

    while True :
        print('wanna play a game of TIC TAC TOE ( Y=[yes] | N=[no] ) :' , end = ' ')
        play_game = input()
        if play_game == 'N':
            print('thank you for your time, i guess i have nothing for you then')
            break
        elif play_game == 'Y':
            print('\n' + 'game begins, get a friend' + '\n')
            print('positions on the board are')
            board_0()
            print('your initial board is blank it looks like this ')
            TTT()
            print('\n' + 'lets start now' + '\n')
            turn = 'x'
            for i in range(9):
                
                print('turn for ' + turn + ' to play')
                print('pick a position to play:', end = ' ')
                
                pos = input()

                game_board[pos] = turn 

                TTT()

                if (game_board['BL'] == game_board['BM'] == game_board['BR'] == turn) == True:
                    print('weldone ' + turn + ' youve won')
                    break

                elif (game_board['TL'] == game_board['TM'] == game_board['TR'] == turn) == True:
                    print('weldone ' + turn + ' youve won')
                    break

                elif (game_board['ML'] == game_board['MM'] == game_board['MR'] == turn) == True:
                    print('weldone ' + turn + ' youve won')
                    break

                elif (game_board['ML'] == game_board['TL'] == game_board['BL'] == turn) == True:
                    print('weldone ' + turn + ' youve won')
                    break

                elif (game_board['MR'] == game_board['TR'] == game_board['BR'] == turn) == True:
                    print('weldone ' + turn + ' youve won')
                    break

                elif (game_board['MM'] == game_board['TM'] == game_board['BM'] == turn) == True:
                    print('weldone ' + turn + ' youve won')
                    break

                elif (game_board['TL'] == game_board['MM'] == game_board['BR'] == turn) == True:
                    print('weldone ' + turn + ' youve won')
                    break

                elif (game_board['TR'] == game_board['MM'] == game_board['BL'] == turn) == True:
                    print('weldone ' + turn + ' youve won')
                    break

                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'


        else :
            print('you provided the wrong input, type either (Y) or (N)')
            print('without the parenthesis please')

game_TTT()

# so first part of the game completed just need to twick somethings
# like stop your turn from being able to write over other peoples turn
# and add in a prompt when the game is a draw 
# yeah that should be all
# oh yeah add time delays to the messages and the printing
# it doesnt look nice the way it prints out all at once.

# bonus things to add- to spice up the game
# the ability to write over peoples turn but not their last turn see how 
# that goes
# and also adding power ups or something like that ionno seems cool and making
# the board a lot longer

    


