#!/bin/python3

if __name__ == '__main__':
    a=set(map(int,input().split()))
    print(all(a.issuperset(set(map(int,input().split()))) for _ in range(int(input()))))