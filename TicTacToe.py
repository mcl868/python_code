import numpy

def theplayer(y):
    if y == 1:
        val="X"
    elif y == 2:
        val="O"
    else:
        val=" "
    return val

print(theplayer(1))
print(theplayer(2))
print(theplayer(3))


def board(x1, x2, x3, x4, x5, x6, x7, x8, x9):
    if x1 == 0:
        x1=" "
    if x2 == 0:
        x2=" "
    if x3 == 0:
        x3=" "
    if x4 == 0:
        x4=" "
    if x5 == 0:
        x5=" "
    if x6 == 0:
        x6=" "
    if x7 == 0:
        x7=" "
    if x8 == 0:
        x8=" "
    if x9 == 0:
        x9=" "
    print("                 |         |         ")
    print("                 |         |         ")
    print("           ",x1,"   |   ",x2,"   |   ",x3,"  ")
    print("                 |         |         ")
    print("        _________|_________|_________")
    print("                 |         |         ")
    print("                 |         |         ")
    print("           ",x4,"   |   ",x5,"   |   ",x6,"  ")
    print("                 |         |         ")
    print("        _________|_________|_________")
    print("                 |         |         ")
    print("                 |         |         ")
    print("           ",x7,"   |   ",x8,"   |   ",x9,"  ")
    print("                 |         |         ")
    print("                 |         |         ")

board("O", "X", 3, 4, 5, 6, 7, 8, 9)

a=[[0,0,0],[0,0,0],[0,0,0]]

print(a)

def field(que):
    if int(que) == 1:
        print(que)
        a[0][0]=que
    if int(que) == 2:
        print(que)
        a[0][1]=que
    if int(que) == 3:
        print(que)
        a[0][2]=que
    if int(que) == 4:
        print(que)
        a[1][0]=que
    if int(que) == 5:
        print(que)
        a[1][1]=que
    if int(que) == 6:
        print(que)
        a[1][2]=que
    if int(que) == 7:
        print(que)
        a[2][0]=que
    if int(que) == 8:
        print(que)
        a[2][1]=que
    if int(que) == 9:
        print(que)
        a[2][2]=que


q=input("Pick a field: ")
print(int(q))
field(que=q)
q=input("Pick a field: ")
print(int(q))
field(que=q)
q=input("Pick a field: ")
print(int(q))
field(que=q)

q=input("Pick a field: ")
print(int(q))
field(que=q)


print(a)

board(a[0][0],a[0][1],a[0][2],
      a[1][0],a[1][1],a[1][2],
      a[2][0],a[2][1],a[2][2])

