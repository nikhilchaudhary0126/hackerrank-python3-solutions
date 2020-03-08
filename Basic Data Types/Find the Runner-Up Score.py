#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max=scndmax=0
    scores=list()
    #find unique list items
    for item in arr:
        if item not in scores:
            scores.append(item)
    scores.sort()
    #sort and print second last element
    print(scores[-2])