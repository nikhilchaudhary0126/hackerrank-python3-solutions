#!/bin/python3
import re

if __name__=="__main__":
    for _ in range(int(input())):
        try:
            #compile rejex ionto object and give bool result
            print(bool(re.compile(input())))
        except re.error:
            print('False')