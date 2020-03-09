#!/bin/python3
from collections import OrderedDict

if __name__ == '__main__':
    items=OrderedDict()
    for _ in range(int(input())):
        item_name,net_price=input().rsplit(' ', 1)
        #get dictionary key, return 0 if key not does not exist
        items[item_name] = items.get(item_name, 0) + int(net_price)
    for key,value in items.items():
        print(key,value)