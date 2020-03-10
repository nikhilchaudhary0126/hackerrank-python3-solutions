#!/bin/python3

if __name__ == '__main__':
    n,m = map(int,input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())
    arr=sorted(arr,key = lambda x:x[k])
    for item in arr:
        print(*item)