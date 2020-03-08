#!/bin/python3

if __name__=="__main__":
    for _ in range(int(input())):
        a,b=input().split()
        #use try block inside loop as the loop will break if kept inside try block
        try:
            print(int(a)//int(b))
        except ZeroDivisionError as e:
            print("Error Code:",e)
        except ValueError as e:
            print("Error Code:",e)