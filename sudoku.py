import random
import numpy



def checkrow(a):
    numbers = numpy.arange(1,len(a)+1)
    s = []
    for i in range(len(a)):
        if numbers[i] not in a:
            s.append(numbers[i])
    return s

def checkfeild(x):
    vec = numpy.array(x).reshape(-1)
    numbers = numpy.arange(1,len(vec)+1)

    s = []
    for i in range(len(vec)):
        if numbers[i] not in vec:
            s.append(numbers[i])
    return s

def feild(a):
    numbers = numpy.arange(1,len(a)+1)
    place = []
    for i in range(len(a)):
        if a[i] == 0:
            place.append(i)
    return place


def checkall(x):
    vec = numpy.array(x).reshape(-1)
    numbers = numpy.arange(1,len(vec)+1)

    res = all(numbers == numpy.array(sorted(vec)))
    return res




def board(x):
    for j in range(9):
       if j == 0:
           print("                    ___________ ___________ ___________")
       if j in numpy.array([3,6,9]):
           print("                   |___________|___________|___________|")
       print("                   |           |           |           |")
       print("                   |  {0}  {1}  {2}  |  {3}  {4}  {5}  |  {6}  {7}  {8}  |".
             format(x[j,0],x[j,1],x[j,2],x[j,3],x[j,4],x[j,5],x[j,6],x[j,7],x[j,8]))

    print("                   |___________|___________|___________|")



line1 = [0,0,4,6,7,8,9,0,2]
line2 = [6,7,2,1,9,5,3,4,0]
line3 = [1,9,8,3,4,2,5,6,7]
line4 = [8,5,9,0,6,1,4,2,3]
line5 = [4,0,6,8,5,3,7,9,1]
line6 = [7,1,3,9,2,0,8,5,6]
line7 = [9,6,1,0,3,7,2,8,4]
line8 = [2,8,0,4,1,9,6,3,5]
line9 = [0,4,5,2,8,6,1,7,9]


mab = numpy.array([line1,line2,line3,line4,line5,line6,line7,line8,line9])

board(mab)

print(checkrow(line1))

print(checkfeild(mab[0:3,0:3]))


print(all(checkfeild(mab[0:3,0:3]) in checkrow(line1)))



def solvesoduku(x):
    b=0
    solved = True
    while solved:
        aa = x
        b = b+1
        aav2 = []
        for j in range(9):
            row = aa[j]

            aaaaaa = random.sample(checkrow(row),len(checkrow(row)))

            f = numpy.array(feild(row))

            for i in range(len(checkrow(row))):
                row[f[i]] = aaaaaa[i]

            aav2.append(row)
        aav3 = numpy.array(aav2)

        solved = (not (checkall(aav3[0:3,0:3]) and
                       checkall(aav3[0:3,3:6]) and
                       checkall(aav3[0:3,6:9]) and
                       checkall(aav3[3:6,0:3]) and
                       checkall(aav3[3:6,3:6]) and
                       checkall(aav3[3:6,6:9]) and
                       checkall(aav3[6:9,0:3]) and
                       checkall(aav3[6:9,3:6]) and
                       checkall(aav3[6:9,6:9]) and
                       checkall(aav3[0:9,0]) and
                       checkall(aav3[0:9,1]) and
                       checkall(aav3[0:9,2]) and
                       checkall(aav3[0:9,3]) and
                       checkall(aav3[0:9,4]) and
                       checkall(aav3[0:9,5]) and
                       checkall(aav3[0:9,6]) and
                       checkall(aav3[0:9,7]) and
                       checkall(aav3[0:9,8])))

    return board(aav3)

def makeboard():
    my_my_list = []
    for l in range(9):
        my_list = []
        print("Row "+str(l+1)+" ")
        for j in range(9):
            my_list.append(int(input("Column "+str(j+1)+" ")))
        my_my_list.append(my_list)

    return numpy.array(my_my_list)


print("")
print("               ____  _      _ ____     ____   _    __ _      _")
print("              / ___ | |    | |  _ \   / __ \ | |  / /| |    | |")
print("             | /    | |    | | | \ \ / /  \ \| |_/ / | |    | |")
print("             | \___ | |    | | |  | | |    | |    /  | |    | |")
print("              \___ \| |    | | |  | | |    | | |\ \  | |    | |")
print("                  \ | |    | | |  | | |    | | | \ \ | |    | |")
print("               ___/ /\ \__/ /| |_/ / \ \__/ /| |  \ \ \ \__/ /")
print("              |____/  \____/ |____/   \____/ |_|   \_\ \____/")
print("")
print("")






line1 = [5,3,4,6,7,8,9,1,0]
line2 = [6,7,2,1,9,5,3,4,0]
line3 = [0,9,8,3,4,2,5,6,7]
line4 = [8,5,9,0,6,1,4,2,3]
line5 = [4,0,6,8,5,3,7,9,1]
line6 = [7,1,3,9,2,0,8,5,6]
line7 = [9,6,1,0,3,7,2,8,4]
line8 = [2,8,0,4,1,9,6,3,5]
line9 = [0,4,5,2,8,6,1,7,9]


mab = numpy.array([line1,line2,line3,line4,line5,line6,line7,line8,line9])

board(mab)
print("")
print("... and the solution is:")
solvesoduku(mab)


'''

mab=makeboard()

print(board(mab))
print(solvesoduku(mab))



b=0
solved = True
while solved:
    aa = numpy.array([line1,line2,line3,line4,line5,line6,line7,line8,line9])
    b=b+1
    aav2 = []
    for j in range(9):
        row = aa[j]

        aaaaaa = random.sample(checkrow(row),len(checkrow(row)))

        f = numpy.array(feild(row))

        for i in range(len(checkrow(row))):
            row[f[i]] = aaaaaa[i]

        aav2.append(row)
    aav3 = numpy.array(aav2)

    solved = (not (checkall(aav3[0:3,0:3]) and
           checkall(aav3[0:3,3:6]) and
           checkall(aav3[0:3,6:9]) and
           checkall(aav3[3:6,0:3]) and
           checkall(aav3[3:6,3:6]) and
           checkall(aav3[3:6,6:9]) and
           checkall(aav3[6:9,0:3]) and
           checkall(aav3[6:9,3:6]) and
           checkall(aav3[6:9,6:9]) and
           checkall(aav3[0:9,0]) and
           checkall(aav3[0:9,1]) and
           checkall(aav3[0:9,2]) and
           checkall(aav3[0:9,3]) and
           checkall(aav3[0:9,4]) and
           checkall(aav3[0:9,5]) and
           checkall(aav3[0:9,6]) and
           checkall(aav3[0:9,7]) and
           checkall(aav3[0:9,8])))

'''
