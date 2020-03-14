#!/bin/python3
from collections import Counter

if __name__ == '__main__':
    _,rooms=input(),map(int,input().split())
    roomcount=Counter(rooms)
    print(min(roomcount, key=roomcount.get))