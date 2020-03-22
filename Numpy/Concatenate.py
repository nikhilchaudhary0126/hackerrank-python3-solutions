#!/bin/python3
import numpy as np

if __name__ == '__main__':
    n,m,_=map(int,input().split())
    arr1,arr2=[],[]
    for _ in range(n):
        arr1.append(list(map(int,input().split())))
    for _ in range(m):
        arr2.append(list(map(int,input().split())))
    array_1 = np.array(arr1)
    array_2 = np.array(arr2)
    print(np.concatenate((array_1, array_2), axis=0))