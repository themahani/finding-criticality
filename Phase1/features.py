#!/usr/bin/env python

"""
Here we write modules that analyze the basketed data
and returns integers or floats to form a dataframe
"""

import numpy as np
from scipy.signal import argrelextrema

def d12 (x, y):
    """ calculate the 1st and 2nd derivatives of data """
    drv1 = np.diff(y) / np.diff(x)
    idrv1 = np.diff(drv1)
    idrv1 = np.insert(idrv1, len(idrv1), 0)
    drv2 = idrv1 / np.diff(x)
    return drv1, drv2

def derivative(x: np.ndarray, y: np.ndarray) -> float:
    pass

def curvature(x: np.ndarray, y: np.ndarray) -> float:
    """ Find the mean curvature of the first half of the data as a label """
    # mask the data for log scale
    mask = (y != 0)
    # implement the log scale
    x = np.log(x[mask])
    y = np.log(y[mask])
    _, curve = d12(x, y)
    return np.mean(curve[:len(curve) // 2 + 1])

def bump(x: np.ndarray, y: np.ndarray):
    """ find number of bumps and inflections points """
    # mask the data for log scale
    mask = (y != 0)
    # implement the log scale
    x = np.log(x[mask])
    y = np.log(y[mask])
    drv1, drv2 = d12(x, y)
    #number of bumps and Inflection Points
    c1 = 0
    c2 = 0
    for i in range(len(drv1)):
        if drv1[i] == 0:
            if i<len(drv1)-2 and drv1[i-1] != 0 and drv1[i+1] != 0 and drv1[i-2] != 0 and drv1[i+2] != 0:
                c1 = c1 + 1
        #Inflection Points
        elif drv2[i] == 0:
            if i< len(drv1) - 1 and drv2[i-1]*drv2[i+1] < 0 :
                c2 = c2 + 1
    return c1, c2

def s_moghimi(x: np.ndarray, y: np.ndarray):
    # mask the data for log scale
    mask = (y != 0)
    # implement the log scale
    x = np.log(x[mask])
    y = np.log(y[mask])
    #moghimi's feature
    s = x
    S = np.sum(s**3) * np.sum(s)/(np.sum(s**2)) **2
    return S

def minmax(x: np.ndarray, y: np.ndarray) -> list:
    yprime=y[np.where(y!=0)]
    z= (y!=0)

    nmin=3
    nmax=3
    minlist=list(argrelextrema(yprime, np.less_equal ,order=nmin))[-1]
    maxlist=list(argrelextrema(yprime, np.greater_equal ,order=nmax))[-1]

    maxi=maxlist[-1]
    mini=minlist[-1]

    if len(minlist)>1:
        for i in range(len(minlist)):
                if mini>= maxi:
                    mini= minlist[-(1+i)]
                else:
                    break
                i+=1

    ymini = np.where(y==yprime[mini])[0][0]
    ymaxi = np.where(y==yprime[maxi])[0][0]

    threshold=30
    if np.abs(ymini-ymaxi)>threshold:
        ymini= -1
        ymaxi= -1

    ysum=y.sum()
    arr= [ymini,ymaxi,np.log(x[ymini]),np.log(x[ymaxi]),np.log(y[ymini]/ysum),np.log(y[ymaxi]/ysum)]
    return arr


def test():
    """ main body to test your code """
    pass


if __name__ == "__main__":
    test()
