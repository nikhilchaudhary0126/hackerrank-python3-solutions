#!/bin/python3
from itertools import combinations_with_replacement

if __name__ == '__main__':
    s,k=input().split()
    print(*list(map(''.join,combinations_with_replacement(sorted(s),int(k)))),sep='\n')