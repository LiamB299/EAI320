# An agent which plays a list of specified responses to a list of two-round histories.
#
# Uses ideas from information in agents submitted to http://www.rpscontest.com
# Written by: L. Strydom
# Updated by: M. Teles
# Last update: 2020-02-17

import numpy as np
import csv

# All the possible histories.
dictionary = [['R', 'R', 'R', 'R'], ['R', 'R', 'R', 'P'],
              ['R', 'R', 'R', 'S'], ['R', 'R', 'P', 'R'],
              ['R', 'R', 'P', 'P'], ['R', 'R', 'P', 'S'],
              ['R', 'R', 'S', 'R'], ['R', 'R', 'S', 'P'],
              ['R', 'R', 'S', 'S'], ['R', 'P', 'R', 'R'],
              ['R', 'P', 'R', 'P'], ['R', 'P', 'R', 'S'],
              ['R', 'P', 'P', 'R'], ['R', 'P', 'P', 'P'],
              ['R', 'P', 'P', 'S'], ['R', 'P', 'S', 'R'],
              ['R', 'P', 'S', 'P'], ['R', 'P', 'S', 'S'],
              ['R', 'S', 'R', 'R'], ['R', 'S', 'R', 'P'],
              ['R', 'S', 'R', 'S'], ['R', 'S', 'P', 'R'],
              ['R', 'S', 'P', 'P'], ['R', 'S', 'P', 'S'],
              ['R', 'S', 'S', 'R'], ['R', 'S', 'S', 'P'],
              ['R', 'S', 'S', 'S'], ['P', 'R', 'R', 'R'],
              ['P', 'R', 'R', 'P'], ['P', 'R', 'R', 'S'],
              ['P', 'R', 'P', 'R'], ['P', 'R', 'P', 'P'],
              ['P', 'R', 'P', 'S'], ['P', 'R', 'S', 'R'],
              ['P', 'R', 'S', 'P'], ['P', 'R', 'S', 'S'],
              ['P', 'P', 'R', 'R'], ['P', 'P', 'R', 'P'],
              ['P', 'P', 'R', 'S'], ['P', 'P', 'P', 'R'],
              ['P', 'P', 'P', 'P'], ['P', 'P', 'P', 'S'],
              ['P', 'P', 'S', 'R'], ['P', 'P', 'S', 'P'],
              ['P', 'P', 'S', 'S'], ['P', 'S', 'R', 'R'],
              ['P', 'S', 'R', 'P'], ['P', 'S', 'R', 'S'],
              ['P', 'S', 'P', 'R'], ['P', 'S', 'P', 'P'],
              ['P', 'S', 'P', 'S'], ['P', 'S', 'S', 'R'],
              ['P', 'S', 'S', 'P'], ['P', 'S', 'S', 'S'],
              ['S', 'R', 'R', 'R'], ['S', 'R', 'R', 'P'],
              ['S', 'R', 'R', 'S'], ['S', 'R', 'P', 'R'],
              ['S', 'R', 'P', 'P'], ['S', 'R', 'P', 'S'],
              ['S', 'R', 'S', 'R'], ['S', 'R', 'S', 'P'],
              ['S', 'R', 'S', 'S'], ['S', 'P', 'R', 'R'],
              ['S', 'P', 'R', 'P'], ['S', 'P', 'R', 'S'],
              ['S', 'P', 'P', 'R'], ['S', 'P', 'P', 'P'],
              ['S', 'P', 'P', 'S'], ['S', 'P', 'S', 'R'],
              ['S', 'P', 'S', 'P'], ['S', 'P', 'S', 'S'],
              ['S', 'S', 'R', 'R'], ['S', 'S', 'R', 'P'],
              ['S', 'S', 'R', 'S'], ['S', 'S', 'P', 'R'],
              ['S', 'S', 'P', 'P'], ['S', 'S', 'P', 'S'],
              ['S', 'S', 'S', 'R'], ['S', 'S', 'S', 'P'],
              ['S', 'S', 'S', 'S']]


# The values in the csv file should be the sequence generated using the output of the GA.
sequence_filename = "rock_sequence.txt" # example CSV file containing a sequence of 81 objects
with open(sequence_filename, newline='') as f:
    reader = csv.reader(f)
    response = list(reader)[0] # The responses to each history, loaded from the generated CSV file.



if input == '':
    history = ['X']*4
    output = np.random.choice(['R', 'P', 'S'])
else:
    history.pop(0)
    history.append(input)
    try:
        index = dictionary.index(history)
        output = response[index]
    except:
        output = np.random.choice(['R', 'P', 'S'])
    history.pop(0)
    history.append(output)
