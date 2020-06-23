import random
import numpy



def check(a):
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

def intersection(list1, list2): 
    return list(set(list1) & set(list2))

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



def solvesoduku(x):
    solved = True
    aa = x
    while solved:
        for j in range(9):
            set1pre = aa[j,0:9]
            set1 = check(set1pre)
            for i in range(9):
                set2pre = aa[0:9,i]
                set2 = check(set2pre)
                if intersection(set1,set2) and aa[j,i] == 0:
                    aa[j,i] = numpy.sum(intersection(set1,set2))
        solved = (not (checkall(aa[0:9,0]) and
                       checkall(aa[0:9,1]) and
                       checkall(aa[0:9,2]) and
                       checkall(aa[0:9,3]) and
                       checkall(aa[0:9,4]) and
                       checkall(aa[0:9,5]) and
                       checkall(aa[0:9,6]) and
                       checkall(aa[0:9,7]) and
                       checkall(aa[0:9,8])))
    return board(aa)


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






line1 = [0,3,4,6,7,8,9,1,0]
line2 = [6,7,0,1,9,5,3,4,0]
line3 = [0,9,8,3,4,0,5,6,7]
line4 = [8,5,9,0,6,1,4,2,3]
line5 = [4,0,6,8,0,3,0,9,1]
line6 = [0,1,3,9,2,0,8,5,6]
line7 = [9,6,1,0,3,7,2,0,4]
line8 = [2,0,0,4,1,9,6,0,5]
line9 = [0,4,5,0,8,0,0,7,9]


mab = numpy.array([line1,line2,line3,line4,line5,line6,line7,line8,line9])

board(mab)
print("")
print("... and the solution is:")
solvesoduku(mab)











'''

def solvesoduku(x):
    b=0
    solved = True
    while solved:
        aa = x
        b = b+1
        aav2 = []
        for j in range(9):
            row = aa[j]

            cr = check(row)

            aaaaaa = random.sample(cr,len(cr))

            f = numpy.array(feild(row))

            for i in range(len(cr)):
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




'''
