#!/bin/python3
from itertools import product

if __name__ == '__main__':
    k,m=map(int,input().split())
    total,arr=0,[]
    for _ in range(k):
        arr.append(list(map(int,input().split()))[1:])
    for item in product(*arr):
        total = max(sum([a*a for a in item])%m,total)
    print(total)