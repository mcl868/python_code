import numpy

def linearReg_formula(response, model):
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

    return intx2y


def linearPred_formula(response, model, predict=None):
    covariates = numpy.array(model)
    dimcol = len(covariates)
    dimrow = len(covariates[0])

    if dimrow < dimcol:
        covariates = covariates.T
        
    coef = linearReg_formula(response,covariates)

    if predict is None:
        predict = model

    covarpredict = numpy.array(predict)
    dimcol = len(covarpredict)
    dimrow = len(covarpredict[0])

    if dimrow < dimcol:
        covarpredict = covarpredict.T

    designmatrix = numpy.concatenate(([numpy.arange(1,len(response)+1)*0+1],covarpredict), axis=0)

    return numpy.dot(coef,designmatrix)

def linearReg(response, model, digits=3):
    numpy.set_printoptions(precision=digits)
    covariates = numpy.array(model)

    coef = linearReg_formula(response, covariates)
    print("Estimate of the coefficient:")
    return coef

def rounddigits(x, digits=3):
    numpy.set_printoptions(precision=digits)
    return x

