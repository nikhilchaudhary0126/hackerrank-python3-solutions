#!/bin/python3

cube = lambda x:x**3 

def fibonacci(n):
    if n==0:
        return []
    elif n==1:
        return [0]
    else:
        fib=[0,1]
        for i in range(1,n-1):
            fib.append(fib[i]+fib[i-1])
        return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))