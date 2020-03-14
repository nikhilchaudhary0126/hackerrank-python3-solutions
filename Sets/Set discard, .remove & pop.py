#!/bin/python3

if __name__ == '__main__':
    _=int(input())
    s=set(map(int, input().split()))
    for _ in range(int(input())):
        operation=input().split()
        if operation[0]=="remove":
            s.remove(int(operation[1]))
        elif operation[0]=="discard":
            s.discard(int(operation[1]))
        elif operation[0]=="pop":
            s.pop()
    print(sum(s))