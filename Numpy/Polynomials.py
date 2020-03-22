#!/bin/python3
import numpy as np

if __name__ == '__main__':
    p,x=np.array(list(map(float,input().split()))),int(input())
    print(np.polyval(p,x))