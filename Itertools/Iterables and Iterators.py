#!/bin/python3
from itertools import combinations

if __name__ == '__main__':
    _,n,k,sum=input(),input().split(),int(input()),0
    n=list(combinations(n,k))
    for item in n:
        if 'a' in item:
            sum+=1
    print(sum/len(n))