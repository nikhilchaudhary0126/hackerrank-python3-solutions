#!/bin/python3

if __name__ == '__main__':
    _,m=input(),set(map(int,input().split()))
    _,n=input(),set(map(int,input().split()))
    print(*sorted(m.symmetric_difference(n)), sep='\n')