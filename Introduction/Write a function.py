#!/bin/python3

#Note: no need to check input constraints for all problems on HackerRank
def is_leap(year):
    leap = False
    if(year%4==0):
        #century year check
        if(year%100==0):
            #century leap year check
            if(year%400==0):
                leap=True
        else:
            leap=True
    return leap

year= int(input())
print(is_leap(year))