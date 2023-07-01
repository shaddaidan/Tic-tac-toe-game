# trying to remember how to write random actions

import random

sample = ['a', 'b', 'c', 'd']

random.choice(sample)



print(random.choice(sample))

for i in range(5):
    random.choice(sample)
    samp = random.choice(sample)

    # ----------------------------------------

    with open("range5.txt", "a") as file:
        file.write(samp + '\n')

    # code above works thats nice