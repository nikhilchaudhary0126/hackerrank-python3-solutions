#!/bin/python3

#For complex number calcultaions please refer complex number arithematic operations
#Below solution is obtained without using the cmath import
import math

class Complex(object):

    def __init__(self, real, imaginary):
        self.real=real
        self.imaginary=imaginary
        
    def __add__(self, no):
        return Complex(self.real+no.real,self.imaginary+no.imaginary)

    def __sub__(self, no):
        return Complex(self.real-no.real,self.imaginary-no.imaginary)

    def __mul__(self, no):
        r=(self.real*no.real)-(self.imaginary*no.imaginary)
        i=(self.real*no.imaginary)+(self.imaginary*no.real)
        return Complex(r,i)

    def __truediv__(self, no):
        r=((self.real*no.real)+(self.imaginary*no.imaginary))/no.sqrmod()
        i=((no.real*self.imaginary)-(self.real*no.imaginary))/no.sqrmod()
        return Complex(r,i)
    
    def mod(self):
        return Complex(math.sqrt(self.sqrmod()),0.00)
        
    def sqrmod(self):
        return (self.real**2+self.imaginary**2)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')