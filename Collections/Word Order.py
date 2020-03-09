#!/bin/python3
from collections import OrderedDict

if __name__=='__main__':
    count=OrderedDict()
    for _ in range(int(input())):
        item=input()
        count[item]=count.get(item, 0)+1
    print(len(count.keys()))
    print(*count.values())