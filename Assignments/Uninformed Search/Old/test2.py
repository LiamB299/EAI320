#!/usr/bin/env python3

"""Depth of the tree"""
depth = 3

"""Search algorithm to be used"""
bfs_dfs = 1

"""Node class which holds a single object and links to children objects (RPS)"""
class Node:
    def __init__(self, name, level):
        self.name = name
        self.children = [Node]

        """Level is used to determine where in the tree the node is, 
            preventing the break sequence being called at the wrong time"""
        self.level = level

    def retLevel(self):
        return self.level

    def returnName(self):
        return self.name

    def returnChild(self, num):
        if self.children is None:
            return 0
        if num == 0:
            return self.children[0]
        elif num == 1:
            return self.children[1]
        else:
            return self.children[2]

    def retChildren(self):
        return self.children

    def setChildren(self, children):
        self.children = children
        return

    


class rps_tree:
    """Initialize variables"""
    def __init__(self, depth):
        self.depth = depth
        self.head = Node("Start", 0)
        self.generate_levels(self.head, depth)

    """Generate the tree recursively"""
    def generate_levels(self, hold, count):
        """no more levels, end recursion"""
        if count == 0:
            return
        else:
            count = count - 1

            """Link children to parent node"""
            children = [Node("R", self.depth-count), Node("P",self.depth-count), Node("S",self.depth-count)]
            hold.setChildren(children)

            self.generate_levels(children[0], count)
            self.generate_levels(children[1], count)
            self.generate_levels(children[2], count)
            return

    """Returns the head of the tree"""
    def ret_head(self):
        return self.head

"""=================================================================================================================="""

def inc_BFS(step = 0):

    if step == 0:
        return ""

    """BFS sequence is generated iteratively using a queue data structure.
            Nodes are read in a FIFO order then, whereby children are appended to the end of the queue.
                The front object is popped from the queue."""
    queue = head.retChildren()

    while len(queue) != 0:
        hold = queue.pop(0)
        output = hold.returnName()
        prev_lev = curr_lev
        curr_lev = hold.retLevel()
        previous = curr
        curr = input

        if previous == curr and prev_lev < curr_lev:
            # print("Break!")
            count = 0
            while previous == curr and count < 20:
                output = breakSeq(curr)
                previous = curr
                curr = input
                count += 1

        if hold.retChildren() != [Node]:
            queue.append(hold.returnChild(0))
            queue.append(hold.returnChild(1))
            queue.append(hold.returnChild(2))




"""=================================================================================================================="""

"""Moving stuff"""

"""In order to know when the break sequence has been found,
            the previous move must be known"""
    previous = 'Y'
    prev_lev = -1
    curr = 'X'
    curr_lev = -1

"""=================================================================================================================="""

"""Create instance"""
rps = rps_tree(depth)
head = rps.ret_head()

"""Initialization move"""
output = ""


"""Returns the beating object for an opponents move"""
def breakSeq(opp):
    if opp == 'R':
        return 'P'
    elif opp == 'P':
        return 'S'
    elif opp == 'S':
        return 'R'

"""=================================================================================================================="""

if bfs_dfs == 0:
    """In order to know when the break sequence has been found,
        the previous move must be known"""
    previous = 'Y'
    prev_lev = -1

    curr = 'X'
    curr_lev = -1

    """BFS sequence is generated iteratively using a queue data structure.
            Nodes are read in a FIFO order then, whereby children are appended to the end of the queue.
                The front object is popped from the queue."""
    queue = head.retChildren()

    while len(queue) != 0:
        hold = queue.pop(0)
        output = hold.returnName()
        prev_lev = curr_lev
        curr_lev = hold.retLevel()
        previous = curr
        curr = input

        if previous == curr and prev_lev < curr_lev:
            #print("Break!")
            count = 0
            while previous == curr and count<20:
                output = breakSeq(curr)
                previous = curr
                curr = input
                count += 1

        if hold.retChildren() != [Node]:
            queue.append(hold.returnChild(0))
            queue.append(hold.returnChild(1))
            queue.append(hold.returnChild(2))

else:
        """A stack is used for the iterative method of DFS.
            The nodes are seperated into two lists: Visited and unvisited.
                When a node's children are appended they are first reversed then appended.
                    This ensures the order remains a stack of LIFO order."""
        output = []
        outputB = []
        visited = [Node]
        unvisited = head.retChildren()

        unvisited.reverse()
        hold = unvisited.pop()

        output = hold.returnName()

        #output.append(hold.retPath())
        #outputB.append(hold.returnName())

        visited.append(hold)

        while len(unvisited)!=0 or len(hold.retChildren())>1:
            inter = hold.retChildren()
            inter.reverse()
            if len(inter)==3:
                unvisited.extend(inter)
            hold = unvisited.pop()
            visited.append(hold)
            #output.append(hold.retPath())
            #outputB.append(hold.returnName())
            output = hold.returnName()

