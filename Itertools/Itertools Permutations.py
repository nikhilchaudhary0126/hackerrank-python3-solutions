#!/bin/python3
from itertools import permutations

if __name__ == '__main__':
    s,k=input().split()
    print(*list(map(''.join,permutations(sorted(s),int(k)))),sep='\n')