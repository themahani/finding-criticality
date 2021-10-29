#!/usr/bin/env python

"""
Here we write modules that analyze the basketed data
and returns integers or floats to form a dataframe
"""

import numpy as np


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
    return np.mean(curve[:len(curve) // 2 - 1])

def bump(x: np.ndarray, y: np.ndarray):
    """ find number of bumps and inflactions points """
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


def test():
    """ main body to test your code """
    pass


if __name__ == "__main__":
    test()
