#!/bin/python3
import numpy as np

if __name__ == '__main__':
    n,m=map(int,input().split())
    a=np.zeros((n,m),int)
    b=np.zeros((n,m),int)
    for i in range(n):
        a[i]=np.array(input().split(),int)
    for i in range(n):
        b[i]=np.array(input().split(),int)
    print(a+b,a-b,a*b,a//b,a%b,a**b,sep='\n')