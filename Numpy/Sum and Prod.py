#!/bin/python3
import numpy as np

if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=np.zeros((n,m),int)
    for i in range(n):
        arr[i]=np.array(input().split())
    print(np.prod(np.sum(arr, axis = 0)))