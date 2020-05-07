import os
import sys

dirname = os.path.dirname(__file__)

exec(open(dirname+"\\simulatedata.py").read())
sys.path.append(dirname+"\\simplefct.py")

from simplefct import linearReg_formula, linearPred_formula, linearReg, rounddigits
import numpy
import pandas
import matplotlib.pyplot as plt



print("")
print("")
print("")
print("########################################################")
print("########################################################")
print("PROGRAM")

def gformula(a0,a1,a2,data):
    model1 = [data["L0"], data["A0"], data["L1"], data["A1"],
              data["L2"], data["A2"], data["L2"]*data["A2"]]
    model2 = [data["L0"], data["A0"], data["L1"], data["A1"]]
    model3 = [data["L0"], data["A0"], data["L0"]*data["A1"]]

    TDpre = data.drop(columns=["A0","A1","A2"])
    TDpre.insert(2, "A0",numpy.arange(1,nbobs+1)*0+a0, True)
    TDpre.insert(4, "A1",numpy.arange(1,nbobs+1)*0+a1, True)
    TDpre.insert(6, "A2",numpy.arange(1,nbobs+1)*0+a2, True)

    predict1 = [TDpre["L0"], TDpre["A0"], TDpre["L1"], TDpre["A1"],
                TDpre["L2"], TDpre["A2"], TDpre["L2"]*TDpre["A2"]]
    predict2 = [TDpre["L0"], TDpre["A0"], TDpre["L1"], TDpre["A1"]]
    predict3 = [TDpre["L0"], TDpre["A0"], TDpre["L0"]*TDpre["A1"]]

    L2hat = linearPred_formula(data["Y"],model1,predict1)

    L1hat = linearPred_formula(L2hat,model2,predict2)
 
    return numpy.mean(linearPred_formula(L1hat,model3,predict3))



b = numpy.array([[gformula(0,0,0,dfCausalData)],
                 [gformula(1,0,0,dfCausalData)],
                 [gformula(0,1,0,dfCausalData)],
                 [gformula(0,0,1,dfCausalData)],
                 [gformula(1,1,0,dfCausalData)],
                 [gformula(1,0,1,dfCausalData)],
                 [gformula(0,1,1,dfCausalData)],
                 [gformula(1,1,1,dfCausalData)]])

A = numpy.array([[1, 0, 0, 0, 0, 0, 0, 0],
                 [1, 1, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0],
                 [1, 0, 0, 1, 0, 0, 0, 0],
                 [1, 1, 1, 0, 1, 0, 0, 0],
                 [1, 1, 0, 1, 0, 1, 0, 0],
                 [1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 1, 1, 1, 1, 1, 1, 1]])


print(rounddigits(numpy.dot(numpy.linalg.inv(A),b).T))








mu, sigma = 0, 1 # mean and standard deviation

repreatsim = []
for i in range(100):
    print(i)
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
    b = numpy.array([[gformula(0,0,0,dfCausalData)],
                     [gformula(1,0,0,dfCausalData)],
                     [gformula(0,1,0,dfCausalData)],
                     [gformula(0,0,1,dfCausalData)],
                     [gformula(1,1,0,dfCausalData)],
                     [gformula(1,0,1,dfCausalData)],
                     [gformula(0,1,1,dfCausalData)],
                     [gformula(1,1,1,dfCausalData)]])
    repreatsim.append(numpy.dot(numpy.linalg.inv(A),b).T)


print(rounddigits(numpy.mean(repreatsim,axis=0)))
