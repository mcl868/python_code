import random
import numpy



def checkfeild(a):
    numbers = [1,2,3,4,5,6,7,8,9]
    s = []
    for i in range(9):
        if numbers[i] not in a:
            s.append(numbers[i])
    return s

def feild(a):
    numbers = [1,2,3,4,5,6,7,8,9]
    place = []
    for i in range(9):
        if a[i] == 0:
            place.append(i)
    return place


def checkall(x):
    numbers = numpy.array([1,2,3,4,5,6,7,8,9])

    res = all(numbers == numpy.array(sorted(numpy.array(x).reshape(-1))))
    return res


def board(x):
    for j in range(9):
       if j == 0:
           print(" _____________ _____________ _____________")
       if j in numpy.array([3,6,9]):
           print("|_____________|_____________|_____________|")
       print("|             |             |             |")
       print("| ",x[j,0]," ",x[j,1]," ",x[j,2],
             " | ",x[j,3]," ",x[j,4]," ",x[j,5],
             " | ",x[j,6]," ",x[j,7]," ",x[j,8]," | ")
       print("|             |             |             |")
    print("|_____________|_____________|_____________|")



line1 = [5,3,0,0,7,8,0,0,0]
line2 = [6,0,0,1,9,5,3,4,8]
line3 = [0,9,8,3,4,2,5,6,7]
line4 = [8,0,9,7,6,1,0,2,3]
line5 = [4,0,6,8,5,3,7,9,1]
line6 = [7,0,3,9,2,4,8,5,6]
line7 = [9,6,1,0,3,7,2,8,4]
line8 = [2,8,7,4,1,9,6,3,5]
line9 = [3,4,5,2,8,6,1,7,9]








b=0
solved = True
while solved:
    aa = numpy.array([line1,line2,line3,line4,line5,line6,line7,line8,line9])
    b=b+1
    aav2 = []
    for j in range(9):
        row = aa[j]
    
        aaaaaa = random.sample(checkfeild(row),len(checkfeild(row)))
            
        f = numpy.array(feild(row))
    
        for i in range(len(checkfeild(row))):
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


print(board(numpy.array([line1,line2,line3,line4,line5,line6,line7,line8,line9])))

print(board(aav3))

