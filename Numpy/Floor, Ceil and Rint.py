#!/bin/python3
import numpy as np

if __name__ == '__main__':
    arr=np.array(input().split(),dtype=float)
    np.set_printoptions(legacy='1.13')
    print(np.floor(arr),np.ceil(arr),np.rint(arr),sep='\n')