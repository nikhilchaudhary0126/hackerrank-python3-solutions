#!/bin/python3
from collections import Counter

if __name__ == '__main__':
    shoes=int(input())
    shoelist=map(int, input().split())
    shoedict=Counter(shoelist) #dictionary of number of shoes
    amnt=0
    for _ in range(0,int(input())):
        prc=list(input().split())
        for item in shoedict.keys():
            #check shoesize and number of shoes
            if (item==int(prc[0]) and shoedict[item]!=0):
                #decrement shoe count and add amount
                shoedict[item]=shoedict[item]-1
                amnt+=int(prc[1])
    print(amnt)