# so the goal here is to calculate how accurate the random function is
# and the see how the accuracy changes as the sample number increases

# steps
# create a random sample of four values (a,b,c,d)
# then run random on it to pick out each value 
# then take count of each value taken 
# now convert the number of times a value(e.g a,b ..) is gotten into %
# then perform the operation for scaled of numbers start with like
# 100 , 1000, 10000 , 100000 and stop where you fell like
# we can check the accuracy of the randomness for all of this

# like the though of a computer program beforming a random action always
# baffled me, like how do you right a wel structured program to perform
#  a random task like how to you right an ordered process to perform a
# a random task, so i came to the conclusion random isnt random isnt an
# an aproximate of a random action

#step one get all we require to make this program
import random

sample = ['a', 'b', 'c', 'd']

for i in range(5):
    random.choice(sample)
    samp = random.choice(sample)

    with open("range5.txt", "a") as file:    # the a mean append and we use it over the w which is write cause the write clears the page each time it writes into it
        file.write(samp)







