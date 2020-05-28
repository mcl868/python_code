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

def fillthefield(a):
    numbers = [1,2,3,4,5,6,7,8,9]
    place = []
    for i in range(9):
        if a[i] == 0:
            place.append(i)
    return place




line1 = [5,3,4,5,7,0,9,1,2]
line2 = [6,7,7,0,9,5,3,4,8]
line3 = [1,0,8,3,4,2,5,6,7]
line4 = [8,5,9,7,6,1,0,0,3]
line5 = [4,2,0,8,5,3,7,9,1]
line6 = [7,0,3,9,2,4,8,5,6]
line7 = [9,6,1,0,3,7,2,8,4]
line8 = [2,8,0,4,1,9,6,3,5]
line9 = [3,4,0,2,8,6,1,7,9]



aa = numpy.array([line1,line2,line3,line4,line5,line6,line7,line8,line9])
print(aa)



aav2 = []
for j in range(9):
    row = aa[j,]

    aaaaaa = random.sample(checkfeild(row),len(checkfeild(row)))

    f = numpy.array(feild(row))
    print(f)


'''

aav2 = []
for j in range(9):
    row = aa[j,]

    aaaaaa = random.sample(checkfeild(row),len(checkfeild(row)))

    f = numpy.array(feild(row))
    
    for i in range(len(checkfeild(row))):
        row[f[i]] = aaaaaa[i]

    aav2.append(row)

aav2 = numpy.array(aav2)

print(numpy.array(aav2[0:3,0:3]))




numbers = [1,2,3,4,5,6,7,8,9]


print(numbers in numpy.array(aav2[0:3,0:3]).reshape(-1) and
      numbers in numpy.array(aav2[3:6,0:3]).reshape(-1) and
      numbers in numpy.array(aav2[6:9,0:3]).reshape(-1))

print(numbers in numpy.array(aav2[0:3,3:6]).reshape(-1) and
      numbers in numpy.array(aav2[3:6,3:6]).reshape(-1) and
      numbers in numpy.array(aav2[6:9,3:6]).reshape(-1))

print(numbers in numpy.array(aav2[0:3,6:9]).reshape(-1) and
      numbers in numpy.array(aav2[3:6,6:9]).reshape(-1) and
      numbers in numpy.array(aav2[6:9,6:9]).reshape(-1))




print(not (numbers in numpy.array(aav2[0:3,0:3]).reshape(-1) and
           numbers in numpy.array(aav2[3:6,0:3]).reshape(-1) and
           numbers in numpy.array(aav2[6:9,0:3]).reshape(-1) and
           numbers in numpy.array(aav2[0:3,3:6]).reshape(-1) and
           numbers in numpy.array(aav2[3:6,3:6]).reshape(-1) and
           numbers in numpy.array(aav2[6:9,3:6]).reshape(-1) and
           numbers in numpy.array(aav2[0:3,6:9]).reshape(-1) and
           numbers in numpy.array(aav2[3:6,6:9]).reshape(-1) and
           numbers in numpy.array(aav2[6:9,6:9]).reshape(-1)))




solved = True
while solved:
    aav2 = []
    for j in range(9):
        row = aa[j]
    
        aaaaaa = random.sample(checkfeild(row),len(checkfeild(row)))
    
        f = numpy.array(feild(row))
    
        for i in range(len(checkfeild(row))):
            row[f[i]] = aaaaaa[i]

        aav2.append(row)

    aav2 = numpy.array(aav2)

    solved=(not (numbers in numpy.array(aav2[0:3,0:3]).reshape(-1) and
            numbers in numpy.array(aav2[3:6,0:3]).reshape(-1) and
            numbers in numpy.array(aav2[6:9,0:3]).reshape(-1) and
            numbers in numpy.array(aav2[0:3,3:6]).reshape(-1) and
            numbers in numpy.array(aav2[3:6,3:6]).reshape(-1) and
            numbers in numpy.array(aav2[6:9,3:6]).reshape(-1) and
            numbers in numpy.array(aav2[0:3,6:9]).reshape(-1) and
            numbers in numpy.array(aav2[3:6,6:9]).reshape(-1) and
            numbers in numpy.array(aav2[6:9,6:9]).reshape(-1)))
aav2






b=0
while b<10:
    b=b+1
    print(b)





def checkfeild33(a):
    numbers = [1,2,3,4,5,6,7,8,9]
    s = []
    for i in range(9):
        if numbers[i] not in a:
            s.append(numbers[i])
    return s


while runque == "y":
        runque = question()
        runque = input("Type Y if you want to ask me another question. ")

print(aa[0:9,0])
print(checkfeild(a=aa[0:9,0]))
print(aa[0,0:9])
print(checkfeild(a=aa[0,0:9]))

print(numpy.array(aav2[0:3,0:3]).reshape(-1))
print(numbers in numpy.array(aav2[0:3,0:3]).reshape(-1))



print(numpy.array(aav2[3:6,0:3]).reshape(-1))
print(numbers in numpy.array(aav2[3:6,0:3]).reshape(-1))

print(aa[3:6,0:3])
print(checkfeild(a=aa[3:6,0:3]))

print(aa[6:9,0:3])
print(checkfeild(a=aa[6:9,0:3]))

print(aa[0:9,0])
print(checkfeild(a=aa[0:9,0]))



aa = [[1,2,3],[4,5,6],[7,8,9]]
print(aa)


print(numpy.sum(aa))

print(aa[0])


columns = list(zip(*aa))

print(columns)

print("column[0] = {}".format(columns[0]))
print("column[1] = {}".format(columns[1]))
print("column[2] = {}".format(columns[2]))

print(columns[0])
print(numpy.sum(columns[0]))

    for i in range(3):
        if numpy.sum(pickdoor) != i:
            if gamedoors[i] == ["goat"]:
                tmpop.append(i)
                if i not in [numpy.sum(pickdoor),opendoor]:
'''
