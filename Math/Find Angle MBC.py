#!/bin/python3

import math

if __name__=='__main__':
    ab=int(input())
    bc=int(input())
    #use tan inverse to get the angle in radians. Convert radians into degrees and roundoff. Covert into string and add °
    print(str(round(math.degrees(math.atan(ab/bc))))+"°")