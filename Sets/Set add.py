#!/bin/python3

if __name__ == '__main__':
    stamps=set()
    for _ in range(int(input())):
        stamps.add(input())
    print(len(stamps))