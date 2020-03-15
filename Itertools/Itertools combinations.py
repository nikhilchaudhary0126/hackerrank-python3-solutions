#!/bin/python3
from itertools import combinations

if __name__ == '__main__':
    s,k=input().split()
    for i in range(1,int(k)+1):
        print(*list(map(''.join,combinations(sorted(s),i))),sep='\n')