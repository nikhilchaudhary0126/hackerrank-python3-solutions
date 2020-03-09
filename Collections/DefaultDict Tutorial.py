#!/bin/python3
from collections import defaultdict

if __name__=='__main__':
    n, m = map(int, input().split())
    d = defaultdict(list)
    #create defaultdict with input
    for i in range(1, n + 1):
        d[input()].append(str(i))
    #print and join the next list inputs
    for i in range(m):
        print(' '.join(d[input()]) or -1)