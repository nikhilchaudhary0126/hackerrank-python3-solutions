#!/bin/python3
import numpy as np

if __name__ == '__main__':
    n=int(input())
    a,b=np.zeros((n,n),int),np.zeros((n,n),int)
    for i in range(n):
        a[i]=np.array(input().split())
    for i in range(n):
        b[i]=np.array(input().split())
    print(np.dot(a,b))