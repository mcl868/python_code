import numpy
import pandas
import math


def prob(x):
    probx = math.exp(x)/(1+math.exp(x))
    return probx

def indi(x,z):
    if x < z:
      va = 1
    elif x == z:
      va = 1
    else:
      va = 0
    return va

nbobs = 10000
numpy.random.seed(3)



mu, sigma = 0, 1 # mean and standard deviation
epsilon = numpy.random.normal(mu, sigma, 100)
X1 = numpy.arange(1,100+1)
ID = numpy.arange(1,100+1)
Y = 1+2*X1+epsilon

simpleData = {"ID":ID, "Y": Y, "X1":X1}
dfsimpleData = pandas.DataFrame(simpleData,
                                columns = ["ID", "Y", "X1"])

print("")
print("The first ten records of the simple data.")
print(dfsimpleData.loc[dfsimpleData["ID"] <= 10])

print("")
print("The name of the data is: dfsimpleData")
print("The intercept is 1.")
print("The coefficient of X1 is 2.")


ID = numpy.arange(1,nbobs+1)

mu, sigma = 0, 1 # mean and standard deviation
epsilon = numpy.random.normal(mu, sigma, nbobs)
X1 = numpy.arange(1,nbobs+1)
p = .5
X2 = numpy.random.binomial(1, p, nbobs)
Y = 9+2*X1-3*X2-1*X1*X2+epsilon

complexData = {"ID":ID, "Y": Y, "X1":X1, "X2":X2, "X1X2":X1*X2}
dfcomplexData = pandas.DataFrame(complexData,
                                 columns = ["ID", "Y", "X1", "X2","X1X2"])

print("")
print("The first ten records of the complex data.")
print(dfcomplexData.loc[dfcomplexData["ID"] <= 10])

print("")
print("The name of the data is: dfsimpleData")
print("The intercept is 9.")
print("The coefficient of X1 is 2.")
print("The coefficient of X2 is -3.")
print("The coefficient of X1*X2 is -1.")


mu, sigma = 0, 1 # mean and standard deviation

L0 = numpy.random.normal(mu, sigma, nbobs)

UA0 = numpy.random.uniform(0,1,nbobs)
A0 = numpy.arange(1,nbobs+1)*0
i = 0
while i < nbobs:
    A0[i] = indi(UA0[i],prob(0.6*L0[i]))
    i += 1

L1 = -A0+0.2*L0-1*A0*L0+numpy.random.normal(mu, sigma, nbobs)

UA1 = numpy.random.uniform(0,1,nbobs)
A1 = numpy.arange(1,nbobs+1)*0
i = 0
while i < nbobs:
    A1[i] = indi(UA1[i],prob(-1+1.6*A0[i]+1.2*L1[i]-0.8*L0[i]-1.6*L1[i]*A0[i]))
    i += 1

L2 = -A1+1*L1-A0+1.2*L0+numpy.random.normal(mu, sigma, nbobs)

UA2 = numpy.random.uniform(0,1,nbobs)
A2 = numpy.arange(1,nbobs+1)*0
i = 0
while i < nbobs:
    A2[i] = indi(UA2[i],prob(1-0.8*L0[i]+1.6*A0[i]+1.2*L1[i]+1.3*A1[i]+0.5*L2[i]+1.6*L1[i]*A1[i]))
    i += 1

Y = 2*L0+3*A0+1*L1+2*A1-2*L2+5*A2+L2*A2+numpy.random.normal(mu, sigma, nbobs)

CausalData = {"ID":ID, "L0": L0, "A0":A0, "L1": L1, "A1":A1,
              "L2": L2, "A2":A2, "Y": Y}
dfCausalData = pandas.DataFrame(CausalData,
                                columns = ["ID","L0","A0","L1","A1","L2","A2","Y"])

print("")
print("The first ten records of the causal data.")
print(dfCausalData.loc[CausalData["ID"] <= 10])


print("")
print("The name of the data is: dfCausalData")
print("The causal effects in the marginal structural model are given by:")
print("The intercept is none.")
print("The causal effect of the exposure at time 0 is 6.")
print("The causal effect of the exposure at time 1 is 4.")
print("The causal effect of the exposure at time 2 is 5.")
print("The causal effect of the interaction between the two exposures at time 0 and time 1 is none.")
print("The causal effect of the interaction between the two exposures at time 0 and time 2 is -2.")
print("The causal effect of the interaction between the two exposures at time 1 and time 2 is -1.")
print("The causal effect of the interaction between all three exposures at time 0, 1 and 2 is none.")


