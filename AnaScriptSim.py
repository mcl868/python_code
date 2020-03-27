import numpy
import pandas
import os
import matplotlib.pyplot as plt 
import sys

dirname = os.path.dirname(__file__)

exec(open(dirname+"\\simulatedata.py").read())
sys.path.append(dirname+"\\simplefct.py")

from simplefct import linearReg_formula, linearPred_formula, linearReg, rounddigits


print("")
print("")
print("")
print("########################################################")
print("########################################################")
print("PROGRAM")


sim = [dfsimpleData["X1"]]
print("")
print("Using linearReg_formula")
print(linearReg_formula(dfsimpleData["Y"],model=sim))

print("")
print("Using linearPred_formula without predictSet")
print(linearPred_formula(dfsimpleData["Y"],model=sim))
print("")
print("Using linearPred_formula")
predictSet=[dfsimpleData["X1"]]
print(linearPred_formula(dfsimpleData["Y"],model=sim,predict=predictSet))

print("")
print("Using linearReg")
print(linearReg(dfsimpleData["Y"],model=sim))

print("")
#Add columns to exiting dataset
dfsimpleData.insert(2, "Yhat", linearPred_formula(simpleData["Y"],sim), True) 
print(dfsimpleData.loc[dfsimpleData["ID"] <= 10])


# plt.plot(dfsimpleData["X1"], linearPred_formula(simpleData["Y"],sim), color = "g")
# plt.scatter(sim, dfsimpleData["Y"], color = "m", marker = "o", s = 30)
# putting labels 
# plt.xlabel('X1') 
# plt.ylabel('Y') 
# plt.show() 
