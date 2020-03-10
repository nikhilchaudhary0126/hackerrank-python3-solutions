#!/bin/python3

if __name__=='__main__':
    n,x= map(int,input().split())
    scores=[]
    for _ in range(x):
        scores.append(input().split())
    for item in zip(*scores):
        sum=0
        for element in item:
            sum+=float(element)
        print('%.2f' % (sum/x))