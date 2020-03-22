#!/bin/python3
import numpy as np

if __name__ == '__main__':
    n=int(input())
    np.set_printoptions(legacy='1.13')
    a=np.zeros((n,n),float)
    for i in range(n):
        a[i]=np.array(input().split(),float)
    print(np.linalg.det(a))