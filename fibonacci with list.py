# -*- coding: utf-8 -*-
"""
Created on Fri May 13 14:56:11 2022

@author: User
"""

def fib(num):
    a=0
    b=1
    fibonacci=[]
    for i in range(num):
        fibonacci.append(a)
        temp=a
        a=b
        b=temp+b
    return fibonacci
print(fib(20))