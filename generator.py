# -*- coding: utf-8 -*-
"""
Created on Wed May 11 20:29:04 2022

@author: User
"""

def generator_func(num):
    for i in range(num):
        yield i*2     
g=generator_func(100)

next(g)
print(next(g))
print(next(g))
print(next(g))