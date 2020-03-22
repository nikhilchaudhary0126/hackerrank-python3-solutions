#!/bin/python3
import numpy as np

if __name__ == '__main__':
    a=np.array(list(map(int,input().split())))
    b=np.array(list(map(int,input().split())))
    print(np.inner(a,b))
    print(np.outer(a,b))