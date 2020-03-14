#!/bin/python3

if __name__ == '__main__':
    _, a = input(), set(input().split())
    _, b = input(), set(input().split())
    print(len(a.symmetric_difference(b)))