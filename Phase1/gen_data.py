#!/usr/bin/env python

""" use everything so far to generate dataframe """

import numpy as np

from features import bump, curvature, minmax, s_moghimi
from labeling import is_critical, paramsplit
from raw_data.read_files import read_files


def main():
    """ main body """
    paths = read_files("raw-data/basket/")
    path = "raw-data/basket/N1000 Hei/y_N1000 j1.5 d1.5 g7.0 w1.975 base9 PA_Hei_pos.npy"




if __name__ == "__main__":
    main()
