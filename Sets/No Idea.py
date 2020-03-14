#!/bin/python3

if __name__ == '__main__':
    _ = input()
    arr_elemets=map(int,input().split())
    a,b,hap=set(map(int,input().split())),set(map(int,input().split())),0
    for item in arr_elemets:
        if item in a:
            hap+=1
        if item in b:
            hap-=1
    print(hap)