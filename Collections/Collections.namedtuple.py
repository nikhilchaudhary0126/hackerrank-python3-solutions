#!/bin/python3
from collections import namedtuple
if __name__=='__main__':
    cntr, Student, total=int(input()),namedtuple('Student',input()),0
    for _ in range(cntr):
        total+=int(Student(*input().split()).MARKS)
    print('%.2f' % (total/cntr))