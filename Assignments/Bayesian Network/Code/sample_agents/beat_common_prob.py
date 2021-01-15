# Play to statistically beat an opponent's most commonly-played object.
#
# Modified from the code available at http://www.rpscontest.com/submit
# The original version always played to always beat the opponent's most commonly-played
#  object.  The updated version plays randomly with probabilities based on the frequency
#  with which the opponent plays each object.
#
# Updated by: W. P. du Plessis
# Last update: 2019-02-10


import random

if input == "": # initialize variables for the first round
    rockCount = paperCount = scissorsCount = 1
elif input == "R":
    rockCount += 1
elif input == "P":
    paperCount += 1
elif input == "S":
    scissorsCount += 1

value = random.randint(1, rockCount + paperCount + scissorsCount)
if value <= rockCount:
    output = "P"
else:
    value -= rockCount
    if value <= paperCount:
        output = "S"
    else:
        output = "R"
