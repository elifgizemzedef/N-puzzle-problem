import copy
import random

import numpy as np


class Node():
    def __init__(self,data=None):
        self.data=data
        self.childs=[]
    def addChild(self,data):
        self.childs.append(data)
class Stack():
    def __init__(self):
        self.list=[]
        self.size=0

    def isEmpty(self):
        if len(self.list)==0:
            return True
        return False
    def push(self,data):

        self.list.append(data)
        self.size=self.size + 1
    def pop(self):
        puzzle=self.list.pop(self.size-1)
        self.size=self.size - 1
        return puzzle
#________________________________________
n = 3  # int(input())
m = n


def puzzle(n):
    array = ["*"]
    for i in range(1, pow(n, 2)):
        array.append(i)
    return np.array(array).reshape(n, n)

nPuzzle=puzzle(n)
print(nPuzzle)
previous_direction = "null"
def choosewheretomove():
    global previous_direction
    global nPuzzle
    for i in range(n):
        for x in range(m):
            directionlist = []
            if nPuzzle[i, x] == "*":
                # print(i , x)
                if i != n - 1:
                    directionlist.append("down")

                if i != 0:
                    directionlist.append("up")

                if x != m - 1:
                    directionlist.append("right")

                if x != 0:
                    directionlist.append("left")
                    # cycle önlemek için direction kontrolü
                while (True):
                    direction = random.choice(directionlist)

                    if previous_direction == "right" and direction == "left":
                        continue
                    if previous_direction == "left" and direction == "right":
                        continue
                    if previous_direction == "up" and direction == "down":
                        continue
                    if previous_direction == "down" and direction == "up":
                        continue
                    else:
                        break
                previous_direction = direction
                # print(direction +" "+previous_direction)
                nPuzzle=swap(i, x, direction,nPuzzle)
                i = n
                x = m

            if x == m:
                break

        if i == n:
            break


def swap(i, j, direction,nPuzzle):
    if direction == "up":
        temp = nPuzzle[i - 1, j]
        nPuzzle[i - 1, j] = nPuzzle[i, j]
        nPuzzle[i, j] = temp
    elif direction == "down":
        temp = nPuzzle[i + 1, j]
        nPuzzle[i + 1, j] = nPuzzle[i, j]
        nPuzzle[i, j] = temp
    elif direction == "right":
        temp = nPuzzle[i, j + 1]
        nPuzzle[i, j + 1] = nPuzzle[i, j]
        nPuzzle[i, j] = temp
    elif direction == "left":
        temp = nPuzzle[i, j - 1]
        nPuzzle[i, j - 1] = nPuzzle[i, j]
        nPuzzle[i, j] = temp
    else:
        print("aha zortladık.")
    return nPuzzle
print("\n\n")
def rastgele():
    for i in range(0,3):
        choosewheretomove()
    return nPuzzle
def control(puzzle,puzzle2):
    a = 0
    control = False
    for i in puzzle:
        b = 0
        for x in i:
            if x == puzzle2[a, b]:
                control = True
            else:
                control = False
                return control
            b = b + 1
        a = a + 1

    return control
def directionlist(puzzle):
    directionlist = []
    index=findcoordinats(puzzle)

    i=index[0]
    x=index[1]

    if i != n - 1:
        directionlist.append("down")

    if i != 0:
        directionlist.append("up")

    if x != m - 1:
        directionlist.append("right")

    if x != 0:
        directionlist.append("left")

    return directionlist
def findcoordinats(puzzle):
    for i in range(0,n):
        for j in range(0,m):
            if puzzle[i,j]=='*':
                return [i,j]
    return []
adim=0
startState=Node()
startState.data=copy.deepcopy(rastgele())
goalState=Node()
goalState.data=copy.deepcopy(rastgele())
parent=startState
def dfs():
    global parent
    s=Stack()
    s.push(startState)
    while not s.isEmpty():
        global adim
        temp=s.pop()
        directions=directionlist(temp.data)
        print(temp.data)
        #print(directions)
        if control(temp.data,goalState.data):
            print("buldu")
            print(adim)
            print(temp)
            return
        coordinats = findcoordinats(temp.data)

        for i in directions:
            data = copy.deepcopy(temp.data)
            childPuzzle=swap(coordinats[0],coordinats[1],i,data)
            temp.addChild(Node(childPuzzle))

        for child in temp.childs:
            if not control(child.data,parent.data):
                #print(child.data)
                s.push(child)
        parent=temp
        adim = adim + 1
        if adim == 10000:
            print("bitti bulamadı")
            return


dfs()

