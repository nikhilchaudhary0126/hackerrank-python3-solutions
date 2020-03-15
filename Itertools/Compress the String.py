#!/bin/python3
from itertools import groupby

if __name__ == '__main__':
    s=input()
    for k, g in groupby(s):
        print((len(list(g)),int(k)),end=' ')