import os
import sys

dirname = os.path.dirname(__file__)

exec(open(dirname+"\\simulatedata.py").read())
sys.path.append(dirname+"\\simplefct.py")

from simplefct import linearReg_formula, linearPred_formula, linearReg, rounddigits
import numpy
import pandas
import matplotlib.pyplot as plt
import statsmodels.api as sm


print("")
print("")
print("")
print("########################################################")
print("########################################################")
print("PROGRAM")

com = [dfcomplexData["X1"], dfcomplexData["X2"],dfcomplexData["X1X2"]]
print("")
print("Using linearReg_formula")
print(linearReg_formula(dfcomplexData["Y"],model=com))

print("")
print("Using linearPred_formula without predictSet")
print(linearPred_formula(dfcomplexData["Y"],model=com))
print("")

print("Using linearPred_formula")
predictSet=[dfcomplexData["X1"], dfcomplexData["X2"],dfcomplexData["X1X2"]]
print(linearPred_formula(dfcomplexData["Y"],model=com,predict=predictSet))

print("")
print("Using linearReg")
print(linearReg(dfcomplexData["Y"],model=com))

print("Add columns to exiting dataset")
dfcomplexData.insert(2, "Yhat", linearPred_formula(dfcomplexData["Y"],com), True) 
print(dfcomplexData.loc[dfcomplexData["ID"] <= 10])

