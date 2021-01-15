#!/usr/bin/env python3

# A depth of two would have two rounds of RPS
depth = 2
bfs_dfs = 0

"""My move given to the other player"""
#output = ""



class Node:
    def __init__(self, name, level):
        self.name = name
        #print(self.name)
        self.children = [Node]
        self.level = level

        # Not a graceful method for knowing the order, but time efficient
        self.parent = ""

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

    def appendParent(self, name):
        self.parent = self.parent+name
        return

    def retPath(self):
        return str(self.parent+self.name)

class rps_tree:

    """In order to know when the break sequence has been found, the previous move must be known"""
    previous = 'X'
    prev_lev = -1
    curr = 'X'
    curr_lev = -1


    def __init__(self, depth):
        self.depth = depth
        self.head = Node("Start", 0)
        self.generate_levels(self.head, depth)

    def generate_levels(self, hold, count):

        #print("Gen: " + hold.retPath() + '\n')

        # no more levels, end recursion
        if count == 0:
            #print("Gen: " + hold.retPath() + '\n')
            return
        else:
            count = count - 1

            #print(count)
            children = [Node("R", self.depth-count), Node("P",self.depth-count), Node("S",self.depth-count)]

            if count < depth -1:
                children[0].appendParent(hold.retPath())
                children[1].appendParent(hold.retPath())
                children[2].appendParent(hold.retPath())

            hold.setChildren(children)
            #print("Gen: " + hold.retPath() + '\n')

            self.generate_levels(children[0], count)
            self.generate_levels(children[1], count)
            self.generate_levels(children[2], count)
            return

    def BFS(self):
        """In order to know when the break sequence has been found, the previous move must be known"""
        previous = 'X'
        prev_lev = -1
        curr = 'X'
        curr_lev = -1
        queue = [Node]
        outputB = []
        global output

        if self.depth == 0:
            return 0

        queue = self.head.retChildren()

        while len(queue) != 0:
            hold = queue.pop(0)

            #output.append(hold.retPath())
            #outputB.append(hold.returnName())

            output = hold.returnName()
            prev_lev = curr_lev
            curr_lev = hold.retLevel()
            previous = curr
            curr = input

            if previous == curr and prev_lev < curr_lev:
                count = 5
                while previous == curr and count<6:
                    output = self.breakSeq(curr)
                    previous = curr
                    curr = input
                    count+=1


            if hold.retChildren()!=[Node]:
                queue.append(hold.returnChild(0))
                queue.append(hold.returnChild(1))
                queue.append(hold.returnChild(2))

        return

    def DFS(self):
        output = []
        outputB = []
        visited = [Node]
        unvisited = self.head.retChildren()

        unvisited.reverse()
        hold = unvisited.pop()
        output.append(hold.retPath())
        outputB.append(hold.returnName())
        visited.append(hold)

        while len(unvisited)!=0 or len(hold.retChildren())>1:
            inter = hold.retChildren()
            inter.reverse()
            if len(inter)==3:
                unvisited.extend(inter)
            hold = unvisited.pop()
            visited.append(hold)
            output.append(hold.retPath())
            outputB.append(hold.returnName())
        return outputB

    def breakSeq(self, opp):
        if opp=='R':
            return 'P'
        elif opp=='P':
            return 'S'
        elif opp=='S':
            return 'R'

rps = rps_tree(depth)
rps.BFS()
