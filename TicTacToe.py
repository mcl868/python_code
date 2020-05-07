import numpy

def theplayer(y):
    if y == 1:
        val="X"
    elif y == 2:
        val="O"
    else:
        val=" "
    return val

def board(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    print("                   |         |         ")
    print("                   |         |         ")
    print("             ",theplayer(x1),"   |   ",theplayer(x2),"   |   ",theplayer(x3),"  ")
    print("                   |         |         ")
    print("          _________|_________|_________")
    print("                   |         |         ")
    print("                   |         |         ")
    print("             ",theplayer(x4),"   |   ",theplayer(x5),"   |   ",theplayer(x6),"  ")
    print("                   |         |         ")
    print("          _________|_________|_________")
    print("                   |         |         ")
    print("                   |         |         ")
    print("             ",theplayer(x7),"   |   ",theplayer(x8),"   |   ",theplayer(x9),"  ")
    print("                   |         |         ")
    print("                   |         |         ")

def field(que,p):
    val = int(que)
    a[val-1] = p

playerseq = [1,2,1,2,1,2,1,2,1]
player = [1,2]

a = [0,0,0,0,0,0,0,0,0]




i = 0
while numpy.sum(a) < 13:
    q=input("Pick a field: ")
    print(numpy.sum(a))
    while a[int(q)-1] == 0:
        field(que=q,p=playerseq[i])
        board(a[0],a[1],a[2],
              a[3],a[4],a[5],
              a[6],a[7],a[8])
    i = i + 1



def check():
    for i in range(3):
        if a[1] == a[i+1] & a[i+1] == a[i+2]:
            return i
        elif a[i] == a[i+3] & a[i+3] == a[i+6]:
            return i+110
        elif a[0] == a[4] & a[4] == a[8]:
            return "Diagonal"
        elif a[2] == a[4] & a[4] == a[6]:
            return "Diagonal"

print(check())



if a[0] == a[1] & a[1] == a[2]:
    print("1!")
if a[3] == a[4] & a[4] == a[5]:
    print("2!")
if a[6] == a[7] & a[7] == a[8]:
    print("3!")

if a[0] == a[3] & a[3] == a[6]:
    print("4!")
if a[1] == a[4] & a[4] == a[7]:
    print("5!")
if a[2] == a[5] & a[5] == a[8]:
    print("6!")

if a[0] == a[4] & a[4] == a[8]:
    print("7!")
if a[2] == a[4] & a[4] == a[6]:
    print("8!")

"""


if a[i+3] == a[i+4] & a[i+4] == a[5]:
    print("2!")
if a[6] == a[7] & a[7] == a[8]:
    print("3!")

if a[0] == a[3] & a[3] == a[6]:
    print("4!")
if a[1] == a[4] & a[4] == a[7]:
    print("5!")
if a[2] == a[5] & a[5] == a[8]:
    print("6!")

if a[0] == a[4] & a[4] == a[8]:
    print("7!")
if a[2] == a[4] & a[4] == a[6]:
    print("8!")




print(a)


q=input("Pick a field: ")
print(int(q))
check(que=q)
field(que=q,p=1)
board(a[0],a[1],a[2],
      a[3],a[4],a[5],
      a[6],a[7],a[8])
q=input("Pick a field: ")
print(int(q))
check(que=q)
field(que=q,p=2)
board(a[0],a[1],a[2],
      a[3],a[4],a[5],
      a[6],a[7],a[8])
q=input("Pick a field: ")
print(int(q))
check(que=q)
field(que=q,p=1)
board(a[0],a[1],a[2],
      a[3],a[4],a[5],
      a[6],a[7],a[8])
q=input("Pick a field: ")
print(int(q))
check(que=q)
field(que=q,p=2)
board(a[0],a[1],a[2],
      a[3],a[4],a[5],
      a[6],a[7],a[8])



for i in range(9):
    print(i)


for i in range(3):
    for j in range(3):
          print(a[i][j])

print(a)

print(a[0])
print(a[1])

print(a[:1])

print(numpy.sum(a, axis = 0))
print(numpy.sum(a, axis = 1))


def field(que,p):
    val = int(que)
    if val == 1:
        a[0][0] = p
    if val == 2:
        a[0][1] = p
    if val == 3:
        a[0][2] = p
    if val == 4:
        a[1][0] = p
    if val == 5:
        a[1][1] = p
    if val == 6:
        a[1][2] = p
    if val == 7:
        a[2][0] = p
    if val == 8:
        a[2][1] = p
    if val == 9:
        a[2][2] = p
"""

