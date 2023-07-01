ran_1 = input()
ran_2 = input()
ran_3 = input()


#  so this doesnt work, wasnt sure why, but i think its because it isnt the same data type i think
if ((ran_1 == ran_2 == ran_3) == ('y')) :
    print( ran_2 + ' won the game')

# this works though so we would use it first, for our game.
if (ran_1 == ran_2 == ran_3) == True :
    print( ran_2 + ' won the game')

# test line for the new one i would be using or implementing i mean
if (ran_1 == ran_2 == ran_3 == 'y') == True :
    print( ran_2 + ' won the game')
# so this 3rd line runs the code we want as we want it noice,
# we got em.

else :
    print('dang it didnt work')
