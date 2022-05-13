# -*- coding: utf-8 -*-
"""
Created on Fri May 13 20:53:34 2022

@author: User
"""

string = input("Original string is ")
x = list(string)
for i in x[0::2]:
    print(i)
    