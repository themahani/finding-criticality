# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:31:10 2021

@author: ROZHIN
"""
import re
import numpy as np

def paramsplit(filepath:str):
    filename= filepath.split('/') #split the directory path
    re_split = re.split('[ a-zA-Z]+',filename[-1]) #split the name of the file, omitting letters
    re_mod = ','.join(s for s in re_split if s).split(',') #omitting white spaces
    params=[float(x) for x in re_mod if x!='_' and x!='.'] #omitting . and _
    return params

def is_critical(filepath: str):
    Size=[1000,2000,4000]
    n=[]
    for i in range(len(Size)):  #the address for phase portrait must be changed
        n.append(np.load('raw-data/regions/phaseportrait_N'+str(Size[i])+'.npy'))
    # x=np.load(filepath)
    data_param = paramsplit(filepath)
    N,w_raw,b= data_param[0], data_param[-2], data_param[-1]
    w=np.floor((w_raw-1) * 40)
    if w>40: w=40
    if b>34: b=34
    label=n[Size.index(int(N))][int(w),int(b)]
    return int(label)

def main():
    """ main body """
    path = "raw-data/basket/N1000 Hei/y_N1000 j1.5 d1.5 g7.0 w1.975 base9 PA_Hei_pos.npy"
    print(paramsplit(path))
    print(is_critical(path))


if __name__ == "__main__":
    main()
