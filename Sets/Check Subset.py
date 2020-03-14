#!/bin/python3

if __name__ == '__main__':
    for _ in range(int(input())):
        _,a=input(),set(map(int,input().split()))
        _,b=input(),set(map(int,input().split()))
        print(a.issubset(b))