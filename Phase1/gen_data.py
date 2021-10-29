#!/usr/bin/env python

""" use everything so far to generate dataframe """

import numpy as np
import pandas as pd

from features import bump, curvature, minmax, s_moghimi
from labeling import is_critical
from raw_data.read_files import read_files


def main():
    """ main body """
    paths = read_files("raw_data/basket/")
    x_files = []
    y_files = []
    for file in paths:
        if 'x' in file:
            x_files.append(file)

    for file in x_files:
        y_files.append(file.replace('x', 'y'))

    # print("x_files: \n", x_files[5])
    # print("\n\n y_files\n", y_files[5])
    for i in range(len(x_files)):
        print(f"Labeling file {i} of {len(x_files)} files...", end="\r")
        x = np.load(x_files[i])
        y = np.load(y_files[i])

        d_bump = bump(x, y)
        d_curvature = curvature(x, y)
        d_mini, d_maxi, d_xmin, d_xmax, d_ymin, d_ymax = minmax(x, y)
        d_s = s_moghimi(x, y)
        label = is_critical(x_files[i])

    x = np.load(x_files[5])
    y = np.load(y_files[5])

    # path = "raw-data/basket/N1000 Hei/y_N1000 j1.5 d1.5 g7.0 w1.975 base9 PA_Hei_pos.npy"




if __name__ == "__main__":
    main()
