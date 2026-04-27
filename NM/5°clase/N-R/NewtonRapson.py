import numpy as np

def MetNR(X,f,df,tol):
    err=1000000
    while err>tol:
        Y=X-(f(X)/df(X))
        err=abs(Y-X)
        X=Y
    return X