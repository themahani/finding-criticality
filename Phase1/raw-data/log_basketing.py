#!/usr/bin/env python
"""
Courtesy of Mahdi Naghiloo
Edited by Ali Mahani :)
"""

from read_files import read_files

import numpy as np
from matplotlib import pyplot as plt


def basketing_special(y: np.ndarray, x_start: int,
        num_of_dots: int, ratio: float=0.5):
    '''
    "num_of_dots" is total number of baskets
    x_start is minimum of our distribution
    y is the probability array and its length is equeal to the number of points in distribution (x_start+i,y[i])
    example:
    pa = np.load(path+'N4000/N4000 j1.5 d1.5 g7.0 w1.0 base0 PA_Hei_pos.npy')
    y = pa[1:]
    x_start = pa[0]

    returned x and z are new array of positions
    each x element is the beginning of basket and each z value is the number(or probability if "y" has been normalized) of that basket
    all arrays are numpy.ndarray type
    '''
    if len(y)<=num_of_dots:
        return np.arange(x_start,x_start+len(y)),y

    if ratio>1 or ratio<0:
        ratio = 0.5

    bin_start_value = int(((x_start)**(ratio)*(len(y)+x_start)**(1-ratio)))
    bin_start_index = bin_start_value - x_start

    if bin_start_index >= num_of_dots:
        num_of_dots = num_of_dots+bin_start_index

    new_bins = np.unique(np.sort(np.logspace(np.log10(bin_start_value),np.log10(len(y)+x_start+1),num_of_dots-bin_start_index).astype(int)))
    num_of_dots = len(new_bins)+bin_start_index

    z = np.empty(num_of_dots)
    x = np.empty(num_of_dots,dtype=int)
    z[:bin_start_index] = y[:bin_start_index]
    x[:bin_start_index] = np.arange(x_start,bin_start_value)
    

    bins2 = np.roll(new_bins,-1)
    dbins = bins2 - new_bins
    x[bin_start_index:] = (new_bins++bins2)/2
        
    for i,j in enumerate(range(bin_start_index,num_of_dots)):
##        z[j] = y[new_bins[i]-x_start:bins2[i]-x_start].sum()/dbins[i]
        z[j] = y[new_bins[i]-x_start:bins2[i]-x_start].mean()

    return x,z


def save_data(x: np.ndarray, y: np.ndarray, filepath: str):
    """ save the arrays in files """
    fp_prefix = "basket/"
    directory_struct = filepath.split('/')
    # print(directory_struct)
    np.save(fp_prefix + directory_struct[1] + "/x_" + directory_struct[-1], x)
    np.save(fp_prefix + directory_struct[1] + "/y_" + directory_struct[-1], y)

def main():
    """ main body """
    filepaths = read_files()    # find all the data files
    num = len(filepaths)

    for index, file in enumerate(filepaths): # loop over all the files
        print(f"Loading file {index} of {num}", end="\r")

        data = np.load(file)
        x_unbasket = np.arange(data[0], data[0] + len(data) - 1)
        y_unbasket = data[1:]
        z_unbasket = (y_unbasket != 0)
        # basketing the data
        x_basket, y_basket = basketing_special(data[1:], data[0], 75, 0.7)

        save_data(x_basket, y_basket, file) # save the data

    # fig , ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 8))

    # ax[0].loglog()
    # ax[0].scatter(x_unbasket[z_unbasket],
    #         y_unbasket[z_unbasket] / y_unbasket.sum(), s=5)
    # ax[0].set_title("raw data")

    # ax[1].loglog()
    # ax[1].scatter(x_basket, y_basket / y_basket.sum(), s=5)
    # ax[1].set_title("basketed data")
    # plt.show()



if __name__ == "__main__":
    main()
