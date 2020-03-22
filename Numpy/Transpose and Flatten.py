#!/bin/python3
import numpy

if __name__ == '__main__':
    n,_=map(int,input().split())
    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))
    nparr=numpy.array(arr)
    print(numpy.transpose(nparr))
    print(nparr.flatten())