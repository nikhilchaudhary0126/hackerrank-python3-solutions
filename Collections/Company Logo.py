#!/bin/python3
from collections import Counter

if __name__ == '__main__':
    chars=dict()
    s=sorted(input())
    #sort the string, then create a dictionary with counts
    for item in s:
        chars[item]=s.count(item)
    #print list having 3 most common characters
    for item in Counter(chars).most_common(3):
        print(*item)