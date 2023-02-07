import random
import numpy as np


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.child = []

#depth=0
def dfs(root):
    #global depth
    #depth = depth + 1
    for i in root.child:
        print(str(i.data)+"\t")
        dfs(i)

#print(str(root.data)+"\n")
#dfs(root)
#print(depth)
#print(root.data)

#get matrix size value from user
n = 3  # int(input())
m = n
#create an array that has "*" value in it
array = ["*"]
#make a listed array
for i in range(1, pow(n, 2)):
    array.append(i)

#make matrix from array
n_puzzle = np.array(array).reshape(n, n)

i=0


previous_direction = "null"
def choosewheretomove():
    global previous_direction
    for i in range(n):
        for x in range(m):
            directionlist = []
            if n_puzzle[i, x] == "*":
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
                swap(i, x, direction,n_puzzle)
                i = n
                x = m

            if x == m:
                break

        if i == n:
            break
sayac = 0
boolcontrol = True
def kontrol(puzzle):
    print("kontrol ediyor")
    global sayac
    if sayac == 10:
        return
    a = 0
    for i in puzzle.data:
        b = 0
        for x in i:
            if x == kontrol_puzzle[a, b]:
                boolcontrol = False
            else:
                boolcontrol = True
                break
            b = b + 1
        if boolcontrol:
            break
        a = a + 1
    # print(n_puzzle, "\n")
    sayac = sayac + 1
    print("kontrol bitti "+ str(sayac))
    return boolcontrol
def dfs(puzzle):
    global previous_direction
    puzzles=[]
    print("buraya geldi")
    if not kontrol(puzzle):
        print("kontrolde bir sıkıntı olabilir")
        return
    directionlist = []
    for i in range(n):
        for x in range(m):

            if n_puzzle[i, x] == "*":
                # print(i , x)
                if i != n - 1:
                    if previous_direction!="up":
                        directionlist.append("down")

                if i != 0:
                    if previous_direction!="down":
                        directionlist.append("up")

                if x != m - 1:
                    if previous_direction!="left":
                        directionlist.append("right")

                if x != 0:
                    if previous_direction!="right":
                        directionlist.append("left")
                i = n
                x = m
            if x == m:
                break
        if i == n:
            break
    for choosen_direction in directionlist:
        temp = swap(i, x, choosen_direction, puzzle.data).copy()
        temp = TreeNode(temp)
        puzzles.append(temp)
        previous_direction = choosen_direction
        print(temp)
        dfs(temp)
    puzzle.child = puzzles

    # print(direction +" "+previous_direction)
    print("seçilen puzzle: ")
    print(puzzle.data)
    print("burada ne yapıyor")
    print(puzzles)
    for possible_puzzles in puzzles:
        print("çocukların çıktısı")
        print(possible_puzzles.data)
        print("\n")
    #for i in puzzle.child:
    #    print("çocuklara gidiyor mu?")
    #    dfs(i)



def swap(i, j, direction,puzzle):
    if direction == "up":
        temp = puzzle[i - 1, j]
        puzzle[i - 1, j] = puzzle[i, j]
        puzzle[i, j] = temp
    elif direction == "down":
        temp = puzzle[i + 1, j]
        puzzle[i + 1, j] = puzzle[i, j]
        puzzle[i, j] = temp
    elif direction == "right":
        temp = puzzle[i, j + 1]
        puzzle[i, j + 1] = puzzle[i, j]
        puzzle[i, j] = temp
    elif direction == "left":
        temp = puzzle[i, j - 1]
        puzzle[i, j - 1] = puzzle[i, j]
        puzzle[i, j] = temp
    else:
        print("aha zortladık.")





for i in range(0, 10):
    choosewheretomove()
kontrol_puzzle = n_puzzle.copy()#randomly generated puzzle (goal)
#mix the puzzle
for i in range(0, 15):
    choosewheretomove()

root= n_puzzle.copy()
root=TreeNode(root)
print("******************************")
print("Goal State")
print(kontrol_puzzle)
print("******************************")
print("Start State")
print(root.data)
dfs(root)

