#!/bin/python3
import numpy

def arrays(arr):
    return numpy.flipud((numpy.array(arr,float)))

if __name__ == '__main__':
    arr = input().strip().split(' ')
    result = arrays(arr)
    print(result)