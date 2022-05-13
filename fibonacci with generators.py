# -*- coding: utf-8 -*-
"""
Created on Thu May 12 22:18:08 2022

@author: User
"""

def fib(num):
    a=0
    b=1
    for i in range(num):
        yield a
        temp=a
        a=b
        b=temp+b
for x in fib(20):
    print(x)