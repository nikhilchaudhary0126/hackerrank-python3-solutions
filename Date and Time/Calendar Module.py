#!/bin/python3
import calendar

if __name__=='__main__':
    month,day,year=map(int,input().split())
    print(calendar.day_name[calendar.weekday(year, month, day)].upper())