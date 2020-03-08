#!/bin/python3
from cmath import phase

if __name__=="__main__":
    vrbl=complex(input())
    print(abs(vrbl))
    print(phase(vrbl))