# An agent which plays from a preset random sequence of objects.  The agent starts from a
# random position in the present sequence each time it is restarted.
#
# Uses ideas from information in agents submitted to http://www.rpscontest.com
# Written by: W. P. du Plessis
# Last update: 2019-02-10


import random

if input == "":

    sequence = ["R","P","S","P","S","R","S","P","R","S","P","S","P","R","S","P","S","R","P","R","S","P","S","R","S","R","S","P","R","S","R","S","P","R","P","S","R","P","S","R","S","R","S","P","R","P","R","S","P","R","S","P","S","P","S","P","S","P","R","S","R","S","R","P","R","S","P","R","P","S","P","S","P","S","P","S","R","S","R","S","P","S","P","S","P","R","S","P","S","P","R","S","R","S","P","R","S","R","P","S","R","S","R","P","S","R","S","P","S","P","R","S","P","S","R","P","S","R","P","S","R","P","R","S","P","R","P","R","P","R","S","R","P","S","R","P","S","R","P","S","P","S","R","S","P","R","S","P","R","P","S","R","P","R","P","S","P","R","P","S","R","S","R","S","R","P","R","P","S","R","P","R","S","P","S","P","R","P","S","R","P","R","P","S","R","S","P","R","P","S","R","S","R","P","R","P","S","R","S","P","S","R","P","R","S","P","S","R","S","P","R","S","P","R","S","R","P","S","R","S","P","R","P","S","P","R","S","R","S","R","P","R","P","S","P","R","S","P","R","S","R","P","R","S","P","S","P","S","R","S","P","S","P","S","P","R","S","R","S","R","P","R","S","P","R","S","R","P","S","R","P","S","R","P","R","P","R","S","R","P","R","P","R","S","R","S","P","R","P","S","R","P","S","P","S","P","R","S","P","R","P","S","R","P","R","S","R","P","S","P","R","P","S","R","S","R","P","R","S","P","S","R","S","R","P","R","P","S","R","P","R","P","S","R","S","P","R","P","S","P","R","S","R","P","R","S","R","S","R","P","S","P","S","R","P","R","S","P","S","P","S","R","P","S","R","P","R","P","S","R","P","R","S","P","S","P","S","P","S","P","S","P","S","P","R","S","P","S","R","S","R","S","P","S","P","R","P","S","R","P","S","P","R","P","S","R","S","R","P","S","R","P","R","P","S","P","S","R","S","R","S","R","P","R","P","R","S","P","R","S","R","P","S","R","S","P","R","S","R","P","S","P","S","R","S","P","S","P","S","P","S","P","R","S","R","S","R","S","R","P","S","R","S","P","S","P","R","P","S","P","S","P","R","P","R","P","S","P","S","R","P","S","P","R","P","S","R","S","P","S","R","P","R","P","R","P","S","P","R","S","R","P","S","P","R","P","R","P","S","P","R","P","R","S","R","S","R","P","R","S","P","S","R","S","R","S","R","S","P","S","R","P","S","R","P","R","P","R","P","R","P","S","P","R","P","S","R","P","R","S","R","P","R","S","R","P","R","P","S","P","R","S","P","S","R","P","S","R","P","R","S","R","P","S","R","P","R","S","P","R","P","S","P","S","R","S","R","S","P","R","S","R","S","R","S","R","P","S","P","R","P","R","P","S","P","S","R","S","R","P","S","R","S","R","P","R","S","P","S","P","R","S","R","S","P","R","P","S","R","S","R","S","R","S","R","P","R","P","S","R","S","R","P","S","R","S","R","P","S","R","S","R","S","P","S","P","R","P","S","P","S","P","S","R","S","R","P","R","P","R","P","S","R","P","S","P","R","S","R","S","R","S","R","P","R","S","P","R","P","R","P","R","P","S","R","S","P","S","P","R","S","R","P","S","P","S","P","S","P","S","R","S","R","P","R","P","R","S","R","S","P","S","R","S","R","P","R","S","P","R","P","R","P","R","P","R","S","R","P","S","P","R","S","R","P","S","R","S","R","P","S","R","S","P","R","P","R","P","S","R","S","R","P","R","S","P","R","P","R","P","S","P","R","P","S","R","S","R","P","R","S","P","R","P","R","S","R","S","R","P","S","P","S","P","S","R","S","R","S","R","S","P","S","R","S","R","S","P","R","S","R","P","S","P","R","S","R","P","R","S","P","R","S","P","S","P","S","R","S","P","S","R","S","P","S","R","S","P","R","P","R","P","S","P","R","S","R","P","S","R","S","P","S","P","R","P","R","S","P","R","P","S","P","R","S","R","P","S","P","R","P","S","R","P","R","S","R","P","S","R","S","R","P","R","P","R","S","P","R","P","R","S","P","S","R","P","S","R","P","R","P","S","P","S","R","P","S","P","R","P","S","R","S","P","R","P","S","P","S","R","P","S","R","S","P","R","S","R","P","R","P","R","P","S","R","P","R","P","R","S","P","S","P","S","R","S","R","S","R","P","R","S","R","S","P","S","R","S","R","S","R","S","P","R","S","R","S","P","S","P","S","R","S","P","R","S","R","S","P","S","R","S","R","S","P","S","R","P","R","P","S","P","R","S","P","S","P","R","S","R"]

    position = random.randint(0, 999)

else:

    position += 1
    if position > 999:
        position = 0


# Play the selected object.
output = sequence[position]
