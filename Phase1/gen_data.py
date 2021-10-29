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

    _data = []
    for i in range(len(x_files)):
        print(f"Labeling file {i} of {len(x_files)} files...", end="\r")
        x = np.load(x_files[i])
        y = np.load(y_files[i])

        d_bump1, d_bump2 = bump(x, y)
        d_curvature = curvature(x, y)
        d_mini, d_maxi, d_xmin, d_xmax, d_ymin, d_ymax = minmax(x, y)
        d_s = s_moghimi(x, y)
        label = is_critical(x_files[i])
        _data.append([d_bump1, d_bump2, d_curvature, d_mini, d_maxi, d_xmin, d_xmax,
                      d_ymin, d_ymax, d_s, label])

    data_frame = pd.DataFrame(_data, columns=['# of bumps', '# of inflections',
        'curvature', 'min i', 'max i', 'x min', 'x max', 'y min', 'y max',
        'S', 'criticality'])
    print("Writing dataframe to csv...")
    data_frame.to_csv('main_data.csv')


    x = np.load(x_files[5])
    y = np.load(y_files[5])

    # path = "raw-data/basket/N1000 Hei/y_N1000 j1.5 d1.5 g7.0 w1.975 base9 PA_Hei_pos.npy"




if __name__ == "__main__":
    main()
