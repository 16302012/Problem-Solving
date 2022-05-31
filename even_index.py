# -*- coding: utf-8 -*-
"""
Created on Tue May 31 20:56:28 2022

@author: User
"""

string = str(input('Original string is: '))
x = list(string)
for i in x[0::2]:
    print(i)