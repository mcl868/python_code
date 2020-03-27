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


