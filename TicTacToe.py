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






a=[[0,0,0],[0,0,0],[0,0,0]]



print(a)
print(numpy.sum(a, axis = 0))

q=input("Pick a field: ")
print(int(q))
field(que=q,p=1)
board(a[0][0],a[0][1],a[0][2],
      a[1][0],a[1][1],a[1][2],
      a[2][0],a[2][1],a[2][2])
q=input("Pick a field: ")
print(int(q))
field(que=q,p=2)
board(a[0][0],a[0][1],a[0][2],
      a[1][0],a[1][1],a[1][2],
      a[2][0],a[2][1],a[2][2])
q=input("Pick a field: ")
print(int(q))
field(que=q,p=1)
board(a[0][0],a[0][1],a[0][2],
      a[1][0],a[1][1],a[1][2],
      a[2][0],a[2][1],a[2][2])
q=input("Pick a field: ")
print(int(q))
field(que=q,p=2)
board(a[0][0],a[0][1],a[0][2],
      a[1][0],a[1][1],a[1][2],
      a[2][0],a[2][1],a[2][2])



for i in range(3):
    for j in range(3):
          print(a[i][j])

print(a)

print(a[0])
print(a[1])

print(a[:1])

print(numpy.sum(a, axis = 0))
print(numpy.sum(a, axis = 1))


