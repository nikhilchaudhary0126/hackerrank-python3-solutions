#!/bin/python3

if __name__ == '__main__':
    _,n=input(),set(map(int,input().split()))
    for _ in range(int(input())):
        operation=input().split()
        otherset=set(map(int,input().split()))
        if operation[0]=='intersection_update':
            n.intersection_update(otherset)
        elif operation[0]=='update':
            n.update(otherset)
        elif operation[0]=='symmetric_difference_update':
            n.symmetric_difference_update(otherset)
        elif operation[0]=='difference_update':
            n.difference_update(otherset)
    print(sum(n))