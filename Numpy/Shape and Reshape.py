#!/bin/python3
import numpy as np

if __name__ == '__main__':
    narr=np.array(list(map(int,input().split())))
    print(narr.reshape(3,3))