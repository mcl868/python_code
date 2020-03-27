#mac: python3.8 -m pip install numpy
#windows: python -m pip install numpy
print("My first document in python")
#print(2+2)

#help("modules")
import statistics
from numpy import matrix
from numpy import linalg
import math
import numpy
import random
import numpy as np
from datetime import date
import random
import pandas as pd
import matplotlib.pyplot as plt



print(" ")
y = numpy.arange(1,11+1)
x = numpy.arange(1,11+1)
print(y)
print(np.sum(y,axis=0)) 


plt.plot(x, y, color = "g") 
  
# putting labels 
plt.xlabel('x') 
plt.ylabel('y') 
  
  # function to show plot 
plt.show() 
plt.close() 

























#print("Estimated coefficients:\nb_0 = {}  \ 
#          \nb_1 = {}".format(b[0], b[1])) 
  
#import sys
#sys.path.append("")


from theOracle import magiceightball



def suma(num1=None,num2=None):
     # make sure user has entered two args and both are numbers
    if num1 is None or num2 is None:
        return "You Must choose two numbers"
    # rest of code

print(suma())




#A = np.array([[2, 0], [0, 5]])
#b = np.array([[8],[1]])
#x = np.array([[1, 2], [4, 5]]) 
#y = np.array([[7, 8], [9, 10]]) 

#print(x)
#print(y)
# using add() to add matrices
#print("The element wise addition of matrix is : ") 
#print(np.add(x,y)) 
  
# using subtract() to subtract matrices 
#print("The element wise subtraction of matrix is : ") 
#print(np.subtract(x,y)) 
  
# using divide() to divide matrices 
#print("The element wise division of matrix is : ") 
#print(np.divide(x,y)) 
#print(np.linalg.inv(x)) 

# using multiply() to multiply matrices element wise 
#print("The element wise multiplication of matrix is : ") 
#print(np.multiply(x,y))

#print(A)
#print(b)
#print(np.multiply(A,b)) 

#print(np.multiply(np.linalg.inv(A),np.multiply(A,b))) 

#print(np.multiply(np.linalg.inv(x),x)) 

  
# using dot() to multiply matrices 
#print("The product of matrices is : ") 
#print(np.dot(x,y)) 

# using sqrt() to print the square root of matrix 
#print("The element wise square root is : ") 
#print(np.sqrt(x)) 
  
# using sum() to print summation of all elements of matrix 
#print("The summation of all matrix element is : ") 
#print(np.sum(y)) 

# using sum(axis=1) to print summation of all columns of matrix 
#print("The row wise summation of all matrix  is : ") 
#print(np.sum(y,axis=1)) 
  
# using "T" to transpose the matrix 
#print("The transpose of given matrix is : ") 
#print(x.T) 

# Fibonacci series:
# the sum of two elements defines the next
#a, b = 0, 1
#while b < 10:
#     print(b)
#     a, b = b, a+b

# Create a vector as a row
vector_row = np.array([1, 2, 3])

# Create a vector as a column
vector_column = np.array([[1],
                          [2],
                          [3]])
now = date.today()
print(now)

import os
dirname = os.path.dirname(__file__)
print(dirname)
prog = dirname+"\simplefct.py"
print(prog)


#cospi = math.cos(math.pi)
#print(cospi)
#logpi = math.log(math.pi)
#print(logpi)

a=np.array([[1,5,6,8],[1,2,5,9],[7,5,6,2]])
print(len(a))
print(len(a[0]))

#ms = statistics.mean([1,1,9,1])
#print(ms)

#mu, sigma = 0, 0.1 # mean and standard deviation
#s = np.random.normal(mu, sigma, 100)
#print(statistics.mean(s))

nbobs = 10
mu, sigma = 0, 1 # mean and standard deviation
epsilon = np.random.normal(mu, sigma, nbobs)
X1 = np.arange(1,nbobs+1)
p = .5
X2 = np.random.binomial(1, p, nbobs)
Y = 9+2*X1-3*X2+epsilon

response =Y
covariates=np.array([X1, X2])
Xbar = numpy.array([np.mean(covariates,axis=1)])
#print(Xbar)
xdiif = numpy.subtract(covariates,Xbar.T)
#print(xdiif)
xy = numpy.dot(xdiif,response)
#print(xy)
x2 = numpy.dot(xdiif,xdiif.T)
#print(x2)

x2xy = numpy.dot(np.linalg.inv(x2),xy)
mat = np.concatenate(([np.arange(1,len(Y)+1)*0+1],covariates), axis=0).T
#print(mat)
intercept = np.array([np.mean(response-numpy.dot(x2xy,covariates))])
#print(intercept)


predi = np.array(numpy.dot(x2xy,covariates))+intercept
#print(predi)

#print(mat.T)
#print(predi)
#print(numpy.dot(mat.T,predi))
#print(mat.T)


print(mat)
print(len(mat))
print(len(mat[0]))

dimcol = len(mat)
dimrow = len(mat[0])
if dimrow > dimcol:
  print("dimrow is greater than dimcol")
elif dimcol == dimrow:
  print("dimcol and dimrow are equal")
else:
  print("dimcol is greater than dimrow")


#print(np.array([X1, X2]).T)

#intercept = np.array([np.mean(response-numpy.dot(x2xy,covariates))])
#print(intercept)
#print(x2xy.T)
#print(np.concatenate((intercept,x2xy), axis=0).T)


#print(np.array(X1))
#print(X1)
cars = {'X1': X1,'X2': X2}

covariates=np.array([X1, X2])
#print(covariates)
#print(np.array([np.arange(1,len(Y)+1)*0+1]))
#print(pd.DataFrame([np.array([np.arange(1,len(Y)+1)*0+1])],[covariates]))

print(np.concatenate(([np.arange(1,len(Y)+1)*0+1],covariates), axis=0).T)
#print(X1)
#print(X2)

#, axis=1

#print(np.array(X1))
#print(cars)
#X = np.array([X1, X2])
#Xbar = np.array([np.mean(X,axis=1)])
#Xbar = np.array([[1],[1]])
#print(X)
#print(Xbar)
#xdiif = np.subtract(X,Xbar.T)
#print(xdiif)
#print(xdiif.T)

#x2 = np.dot(xdiif,xdiif.T)
#print(x2)
#xy = np.dot(xdiif,Y)
#print(xy)

#x2 = np.dot(xdiif,xdiif.T)
#print(x2)
#x2xy = np.dot(np.linalg.inv(x2),xy)
#print(x2xy)


#xdiif = (np.subtract(X,np.mean(X,axis=1)))
#print(xdiif)
#print(xdiif.T)


#x2 = np.multiply(xdiif,xdiif.T)

#print(x2)
def linearreg(response, covariate):
   "This changes a passed list into this function"
   covariates
   Xbar = np.array([np.mean(covariates,axis=1)])
   xdiif = np.subtract(covariates,Xbar.T)

   xy = np.dot(xdiif,Y)
   x2 = np.dot(xdiif,xdiif.T)

   x2xy = np.dot(np.linalg.inv(x2),xy)
   print ("Values inside the function: ", x2xy.T)
   return

# Now you can call changeme function
mylist = [10,20,30];
linearreg(Y,np.array([X1, X2]));


numpy.arange(1,11+1)*0+1


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



#print(y.T)
#ty = y.transpose()
#print(ty)
#print(y)
#print(statistics.mean(x))
#print(statistics.mean(x)-x)
#print(sum(statistics.mean(x)-x))

#xy = sum(np.multiply(X-statistics.mean(X),Y.T))
#print(xy)
#x2 = sum(np.multiply(X-statistics.mean(X),(X-statistics.mean(X)).T))
#print(x2)

#print(xy/x2)





#simData = {'Y': y, 'X':x }






#dfsim = pd.DataFrame(simData, columns = ['Y', 'X'])


#dfsim.to_csv (r'path/dfsim_dataframe.csv', index = False, header=True)

#dfsimi = pd.read_csv (r'path/dfsim_dataframe.csv')

#print(dfsim)
#print (dfsimi)




#print(statistics.mean(s))


def suma(num1=None,num2=None):
     # make sure user has entered two args and both are numbers
    if num1 is None or num2 is None:
        return "You Must choose two numbers"
    # rest of code



# Function definition is here
#def changeme( mylist ):
#   "This changes a passed list into this function"
#   mylist.append([1,2,3,4]);
#   print ("Values inside the function: ", mylist)
#   return

# Now you can call changeme function
#mylist = [10,20,30];
#changeme( mylist );

#math.fsum([1,1,1,1])

#loc = np.array([100.,100.])
#vel = np.array([30.,10])
#loc+=vel
#print(loc)


#cars = {'Brand': ['Honda Civic','Toyota Corolla','Ford Focus','Audi A4'],
#        'Price': [32000,35000,37000,45000]
#        }

#dfe = pd.DataFrame(cars, columns = ['Brand', 'Price'])


#dfe.to_csv (r'/path/texport_dataframe.csv', index = False, header=True)


#dfi = pd.read_csv (r'path/texport_dataframe.csv')
#print (dfe)
#print (dfi)


#########################################################


response = dfsimpleData["Y"]
model = sim
predict = predictSet

covariates = numpy.array(model)
dimcol = len(covariates)
dimrow = len(covariates[0])
if dimrow < dimcol:
    covariates = covariates.T

Xbar = numpy.array([numpy.mean(covariates,axis=1)])
xdiif = numpy.subtract(covariates,Xbar.T)

xy = numpy.dot(xdiif,response)
x2 = numpy.dot(xdiif,xdiif.T)
x2xy = numpy.dot(numpy.linalg.inv(x2),xy)

intercept = numpy.array([numpy.mean(response-numpy.dot(x2xy,covariates))])
intx2y = numpy.concatenate((intercept,x2xy), axis=0)

print(intx2y)

covarpredict = numpy.array(predict)
dimcol = len(covarpredict)
dimrow = len(covarpredict[0])

if dimrow < dimcol:
    covarpredict = covarpredict.T


w = numpy.concatenate(([numpy.arange(1,len(response)+1)*0+1],covarpredict), axis=0)
residual = response-numpy.dot(intx2y,w)
varRes = numpy.var(residual)
print(varRes)
sortResnorm = sorted(residual/varRes)

x = numpy.array([[1, 2], [4, 5]]) 
y = numpy.array([[7, 8], [9, 10]])
print(x)
print(y)
print(numpy.multiply(x,y))


#print(w)
#print(w[:,0])
#print(w[:,0].T)
#print(residual)
#print(residual[0])

print(numpy.dot(w,w.T))
A = numpy.zeros((len(w),len(w)))
numpy.fill_diagonal(A, numpy.mean(w,axis=1))
#print(A)

#print(numpy.linalg.inv(A))
#print(numpy.linalg.inv(A).T)

Avar = numpy.zeros((len(w),len(w)))
numpy.fill_diagonal(Avar, varRes)
#print(Avar)

#print(numpy.dot(numpy.dot(numpy.linalg.inv(A),Avar),numpy.linalg.inv(A).T))




#
#print(residual)
#print(varRes)
#print(residual/varRes)
#print(sortResnorm)


#print(numpy.arange(-1,3,1))

#plt.plot(dfsimpleData["X1"],sortResnorm, color = "g")
# plt.scatter(sim, dfsimpleData["Y"], color = "m", marker = "o", s = 30)
# putting labels 
#plt.xlabel('X1') 
#plt.ylabel('Y') 
#plt.show() 

#print(numpy.pi)
#print(numpy.sqrt(numpy.pi))
#print(2**2)
#def normaldensity(x, mu, sigma):
#    densityv = math.exp(-(x-mu)**2/(2*sigma**2))/numpy.sqrt(2*numpy.pi*sigma**2)
#    return densityv
#
#print(normaldensity(0,0,1))




