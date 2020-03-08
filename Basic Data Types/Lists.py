#!/bin/python3

if __name__ == '__main__':
    inputList=list()
    for _ in range(int(input())):
        a=str(input()).split()
        if a[0]=="insert":
            inputList.insert(int(a[1]),int(a[2]))
        elif a[0]=="print":
            print(inputList)
        elif a[0]=="remove":
            inputList.remove(int(a[1]))
        elif a[0]=="append":
            inputList.append(int(a[1]))
        elif a[0]=="sort":
            inputList.sort()
        elif a[0]=="pop":
            inputList.pop()
        elif a[0]=="reverse":
            inputList.reverse()