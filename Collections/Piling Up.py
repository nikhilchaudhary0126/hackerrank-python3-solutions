#!/bin/python3
from collections import deque

def check(deque):
    for _ in range(len(deque) - 1):
        if deque[0]>=deque[1]:
            deque.popleft()
        elif deque[-1]>=deque[-2]:
            deque.pop()
        else:
            return "No"
    return "Yes"

if __name__ == '__main__':
    for _ in range(int(input())):
        dlength,d=int(input()),deque(map(int,input().split()))        
        print(check(d))