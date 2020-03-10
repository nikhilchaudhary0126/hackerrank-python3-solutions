#!/bin/python3

if __name__=='__main__':
    n, integers=input(),input().split()
    print(all([int(i) > 0 for i in integers]) and any([j == j[::-1] for j in integers]))