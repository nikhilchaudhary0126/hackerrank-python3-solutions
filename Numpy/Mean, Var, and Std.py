#!/bin/python3
import numpy as np

if __name__ == '__main__':
    n,m=map(int,input().split())
    arr=np.zeros((n,m),int)
    np.set_printoptions(legacy='1.13')
    for i in range(n):
        arr[i]=np.array(input().split())
    print(np.mean(arr,axis=1),np.var(arr,axis=0),np.std(arr,axis=None),sep='\n')