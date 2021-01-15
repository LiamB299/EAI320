# An agent which otherwise plays randomly, but without ever repeating its previously-played object.
#
# Uses ideas from information in agents submitted to http://www.rpscontest.com
# Written by: W. P. du Plessis
# Last update: 2019-02-07


import random

if input == "":

    # Play randomly.
    previous = random.choice(["R", "P", "S"])
    
else:

    # Play randomly without repeating the previous card.
    if previous == "R":
        previous = random.choice(["P", "S"])
    elif previous == "P":
        previous = random.choice(["R", "S"])
    else:
        previous = random.choice(["R", "P"])


output = previous
#print output
