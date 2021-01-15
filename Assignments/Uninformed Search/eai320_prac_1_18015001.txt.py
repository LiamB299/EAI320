#!/usr/bin/env python3
import time as time
import random

"""Depth of the tree"""
depth = 5
break_seq = ""

"""Search algorithm to be used"""
bfs_dfs = 1

"""Node class which holds a single object and links to children objects (RPS)"""
class Node:
    def __init__(self, name):
        self.name = name
        self.children = [Node]
        self.parent = ""

    """returns object associated with node"""
    def returnName(self):
        return self.name

    """Returns each child node seperately, 
        0 = R, 1 = P, 2 = S"""
    def returnChild(self, num):
        if len(self.children)==0 or num>2:
            return [Node]
        elif num == 0:
            return self.children[0]
        elif num == 1:
            return self.children[1]
        elif num == 2:
            return self.children[2]

    """Return all children nodes at once"""
    def retChildren(self):
        if len(self.children)==0:
            return [Node]
        else:
            return self.children

    """Link children to parent"""
    def setChildren(self, children):
        self.children = children
        return

    """Used to generate sequence of node"""
    def appendParent(self, name):
        self.parent = self.parent+name
        return

    """Return the complete sequence of the note"""
    def retPath(self):
        return str(self.parent+self.name)


"""Class which holds and generates RPS tree"""
class rps_tree:
    """Initialize variables"""

    def __init__(self, depth):
        self.depth = depth
        self.head = Node("Start")
        self.generate_levels(self.head, depth)

    """Generate the tree recursively"""
    def generate_levels(self, hold, count):
        """no more levels, end recursion"""
        if count == 0:
            return
        else:
            """Count down the levels"""
            count = count - 1

            """Link children to parent node"""
            children = [Node("R"), Node("P"), Node("S")]

            """Generate sequences of nodes"""
            if count < depth -1:
                children[0].appendParent(hold.retPath())
                children[1].appendParent(hold.retPath())
                children[2].appendParent(hold.retPath())

            """Link children to parent"""
            hold.setChildren(children)

            """Recursive call"""
            self.generate_levels(children[0], count)
            self.generate_levels(children[1], count)
            self.generate_levels(children[2], count)
            return

    """Returns the head of the tree"""
    def ret_head(self):
        return self.head

"""=================================================================================================================="""
"""Returns the beating object for an opponents move"""
def WinMove(opp):
    if opp == 'R':
        return 'P'
    elif opp == 'P':
        return 'S'
    elif opp == 'S':
        return 'R'
"""=================================================================================================================="""

"""Initialization move"""
if input == "":

    """Create instance"""
    rps = rps_tree(depth)
    head = rps.ret_head()

    """Initialize variables to be used"""
    prev = "Y"
    curr = "X"
    break_seq = ""
    prev_seq = ""
    currSeq = ""
    check = []
    output = ''

    repeat = False
    break_play = False
    breaking = False

    count = 0

    """Initialize first move for each respective search method, 
        explanation on implementation is further down"""
    if bfs_dfs == 0:
        queue = [Node]
        queue = head.retChildren()

        hold = queue.pop(0)
        queue.extend(hold.retChildren())

        #print("Children Post: " + str(len(queue)))
        output = hold.returnName()

    else:
        unvisited = head.retChildren()
        unvisited.reverse()
        hold = unvisited.pop()
        inter = hold.retChildren()
        inter.reverse()
        unvisited.extend(inter)

        output = hold.retPath()
else:

    #print("Reset")
    prev = curr
    curr = input
    #print("previous: "+prev + " current: "+curr)

    """If the break sequence is known, no searching is needed.
        Play the sequence and then play the beating repeated move"""
    if break_seq != "":

        """Play the beating repeated move"""
        if curr == prev:
            #print("Exploit")
            output = WinMove(prev)

            """Play the next object in the sequence"""
        elif break_play == True:
            #print("Play break sequence")
            if len(check)-1 == 0:
                break_play = False
            output = check.pop(0)

            """Begin playing the objects from the sequence"""
        else:
            #print("Restart sequence")
            check = list(break_seq)
            break_play = True

        """Two repeat rounds are played, this allows a chance to check if the sequence is correct before playing the next sequence"""
    elif (count != 0 and repeat == True) and breaking == False:
        count -=1
        #print("Repeat round play: " + check[0])
        output = check.pop(0)

        """The sequence is observed to be correct, 
            when the sequence repeats on the intermediate repeat round"""
    elif (prev == curr and repeat == True) and breaking == False:
        #print("Repeat round break check")
        """Assign the found sequence as the break sequence"""
        break_seq = currSeq
        repeat = False
        #print("Break: " + currSeq)
        """Set the break flag, no more searching is required"""
        breaking = True
        output = WinMove(prev)

        """If the sequence randomly begins repeating due to an early break sequence play"""
    elif (prev == curr and repeat == False) and breaking == False:
        #print("Play wrong break")
        output = WinMove(prev)

        """On the repeat rounds, no  break sequence was found, searching may continue"""
    elif (prev != curr and repeat == True) and breaking == False:
        #print("No break on repeat round")
        repeat = False
        output = check.pop(0)

        """Acquire the next sequence using BFS"""
    elif (len(check) == 0 and bfs_dfs == 0) and breaking == False:
        """BFS sequence is generated iteratively using a queue data structure.
            Nodes are read in a FIFO order, whereby children are appended to the end of the queue.
            The front object is popped from the queue."""

        """If no sequence is being checked"""
        if len(queue) != 0:

            """Receive next sequence, pop front object"""
            hold = queue.pop(0)
            prev_seq = currSeq
            currSeq = hold.retPath()
            check = list(currSeq)

            """Append children to the end of the queue"""
            if hold.retChildren != [Node]:
                queue.extend(hold.retChildren())
                #print("Children Post: " + str(len(queue)))

        """Acquire the next sequence using DFS"""
    elif (len(check) == 0 and bfs_dfs == 1) and breaking == False:

        """A stack is used for the iterative method of DFS.
            The nodes are stored in unvisited.
            When a node's children are appended they are first reversed in inter then appended.
            This ensures the order remains a stack of LIFO order."""

        """Pop front element, reverse and append it's children via inter to unvisited"""
        if len(unvisited) != 0:
            hold = unvisited.pop()
            inter = hold.retChildren()
            inter.reverse()
            if len(inter) == 3:
                unvisited.extend(inter)
            prev_seq = currSeq
            currSeq = hold.retPath()
            check = list(currSeq)

    """Check holds the current sequence being checked, 
        when check becomes empty the next sequence is loaded using BFS/DFS"""
    if (len(check) > 0 and repeat == False) and breaking == False:
        #print("Play object: " + check[0] + " from sequence: " + currSeq)
        next = check.pop(0)

        """Load the repeating objects which will be played on repeating rounds"""
        if len(check) == 0:
            check.append("R")
            check.append("R")
            count = 1
            #print("Repeat round")
            repeat = True
        output = next

        """If the current object is repeating and has not been picked up in another statement,
            to ensure an output is always given"""
    elif curr == prev:
        output = WinMove(prev)

    #time.sleep(1)




########################################################################################################################
#Test runs output for BFS:

#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.62 seconds

#breakable.py: won 40.0% of matches (4 of 10)
#    won 33.2% of rounds (3319 of 10000)
#    avg score -3.9, net score -39.0

#Test3.py: won 60.0% of matches (6 of 10)
#    won 33.6% of rounds (3358 of 10000)
#    avg score 3.9, net score 39.0

#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#breakable.py: won 40.0% of matches (4 of 10)
#    won 33.1% of rounds (3307 of 10000)
#    avg score -5.4, net score -54.0
#
#Test3.py: won 60.0% of matches (6 of 10)
#    won 33.6% of rounds (3361 of 10000)
#    avg score 5.4, net score 54.0
#
#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.62 seconds

#breakable.py: won 10.0% of matches (1 of 10)
#    won 33.1% of rounds (3312 of 10000)
#    avg score -8.8, net score -88.0

#Test3.py: won 80.0% of matches (8 of 10)
#    won 34.0% of rounds (3400 of 10000)
#    avg score 8.8, net score 88.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.64 seconds

#breakable.py: won 30.0% of matches (3 of 10)
#    won 32.9% of rounds (3291 of 10000)
#    avg score -8.4, net score -84.0

#Test3.py: won 70.0% of matches (7 of 10)
#    won 33.8% of rounds (3375 of 10000)
#    avg score 8.4, net score 84.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.62 seconds

#breakable.py: won 40.0% of matches (4 of 10)
#    won 33.0% of rounds (3300 of 10000)
#    avg score -8.5, net score -85.0

#Test3.py: won 60.0% of matches (6 of 10)
#    won 33.9% of rounds (3385 of 10000)
#    avg score 8.5, net score 85.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#breakable.py: won 20.0% of matches (2 of 10)
#    won 32.5% of rounds (3248 of 10000)
#    avg score -16.4, net score -164.0

#Test3.py: won 80.0% of matches (8 of 10)
#    won 34.1% of rounds (3412 of 10000)
#    avg score 16.4, net score 164.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.64 seconds

#breakable.py: won 10.0% of matches (1 of 10)
#    won 32.5% of rounds (3251 of 10000)
#    avg score -19.3, net score -193.0

#Test3.py: won 90.0% of matches (9 of 10)
#    won 34.4% of rounds (3444 of 10000)
#    avg score 19.3, net score 193.0

########################################################################################################################

#DFS output

#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.64 seconds

#breakable.py: won 10.0% of matches (1 of 10)
#    won 32.7% of rounds (3272 of 10000)
#    avg score -11.7, net score -117.0

#Test3.py: won 90.0% of matches (9 of 10)
#    won 33.9% of rounds (3389 of 10000)
#    avg score 11.7, net score 117.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.62 seconds

#breakable.py: won 20.0% of matches (2 of 10)
#    won 32.9% of rounds (3288 of 10000)
#    avg score -12.7, net score -127.0

#Test3.py: won 80.0% of matches (8 of 10)
#    won 34.2% of rounds (3415 of 10000)
#    avg score 12.7, net score 127.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.62 seconds

#Test3.py: won 40.0% of matches (4 of 10)
#    won 33.5% of rounds (3348 of 10000)
#    avg score -2.4, net score -24.0

#breakable.py: won 50.0% of matches (5 of 10)
#    won 33.7% of rounds (3372 of 10000)
#    avg score 2.4, net score 24.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.62 seconds

#breakable.py: won 0.0% of matches (0 of 10)
#    won 32.6% of rounds (3257 of 10000)
#    avg score -13.2, net score -132.0

#Test3.py: won 90.0% of matches (9 of 10)
#    won 33.9% of rounds (3389 of 10000)
#    avg score 13.2, net score 132.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.65 seconds

#breakable.py: won 50.0% of matches (5 of 10)
#    won 33.0% of rounds (3298 of 10000)
#    avg score -5.2, net score -52.0

#Test3.py: won 50.0% of matches (5 of 10)
#    won 33.5% of rounds (3350 of 10000)
#    avg score 5.2, net score 52.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#Test3.py: won 40.0% of matches (4 of 10)
#    won 33.2% of rounds (3316 of 10000)
#    avg score -1.7, net score -17.0

#breakable.py: won 60.0% of matches (6 of 10)
#    won 33.3% of rounds (3333 of 10000)
#    avg score 1.7, net score 17.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#Test3.py: won 40.0% of matches (4 of 10)
#    won 33.3% of rounds (3332 of 10000)
#    avg score 5.1, net score 51.0

#breakable.py: won 60.0% of matches (6 of 10)
#    won 32.8% of rounds (3281 of 10000)
#    avg score -5.1, net score -51.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#breakable.py: won 20.0% of matches (2 of 10)
#    won 33.0% of rounds (3299 of 10000)
#    avg score -11.8, net score -118.0

#Test3.py: won 80.0% of matches (8 of 10)
#    won 34.2% of rounds (3417 of 10000)
#   avg score 11.8, net score 118.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#breakable.py: won 30.0% of matches (3 of 10)
#    won 33.0% of rounds (3301 of 10000)
#    avg score -9.3, net score -93.0

#Test3.py: won 70.0% of matches (7 of 10)
#    won 33.9% of rounds (3394 of 10000)
#    avg score 9.3, net score 93.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#breakable.py: won 40.0% of matches (4 of 10)
#    won 33.0% of rounds (3296 of 10000)
#    avg score -7.1, net score -71.0

#Test3.py: won 60.0% of matches (6 of 10)
#    won 33.7% of rounds (3367 of 10000)
#    avg score 7.1, net score 71.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#breakable.py: won 40.0% of matches (4 of 10)
#    won 32.9% of rounds (3290 of 10000)
#    avg score -8.7, net score -87.0

#Test3.py: won 50.0% of matches (5 of 10)
#    won 33.8% of rounds (3377 of 10000)
#    avg score 8.7, net score 87.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#breakable.py: won 50.0% of matches (5 of 10)
#    won 33.7% of rounds (3367 of 10000)
#    avg score -2.8, net score -28.0

#Test3.py: won 50.0% of matches (5 of 10)
#    won 34.0% of rounds (3395 of 10000)
#    avg score 2.8, net score 28.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.62 seconds

#breakable.py: won 40.0% of matches (4 of 10)
#    won 33.2% of rounds (3322 of 10000)
#    avg score -2.9, net score -29.0

#Test3.py: won 60.0% of matches (6 of 10)
#    won 33.5% of rounds (3351 of 10000)
#    avg score 2.9, net score 29.0


#C:\Users\liamb\Documents\University\2020\EAI\Practical 1>py rpsrunner.py breakable.py Test3.py
#Pool 1: 1 bots loaded
#Pool 2: 1 bots loaded
#Playing 10 matches per pairing.
#Running matches in 1 threads
#10 matches run
#total run time: 0.63 seconds

#breakable.py: won 30.0% of matches (3 of 10)
#    won 32.9% of rounds (3286 of 10000)
#    avg score -11.8, net score -118.0

#Test3.py: won 70.0% of matches (7 of 10)
#    won 34.0% of rounds (3404 of 10000)
#    avg score 11.8, net score 118.0

