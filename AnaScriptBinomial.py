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

binom_model = sm.GLM(dfCausalData["A0"], dfCausalData["L0"], family=sm.families.Binomial())
binom_model_results = binom_model.fit()
print(binom_model_results.summary())


