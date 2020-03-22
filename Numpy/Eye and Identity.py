#!/bin/python3
import numpy as np
#we are using printoptions to avoid the formatting bug in testcases

if __name__ == '__main__':
    n,m=map(int,input().split())
    np.set_printoptions(legacy='1.13')
    print(str(np.eye(n,m,0)))