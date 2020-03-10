#!/bin/python3

if __name__=='__main__':
    print(*sorted(input(), key=lambda x: (x.isdigit() - x.islower(), x in '02468', x)), sep='')