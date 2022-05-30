# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:29:42 2022

@author: User
"""

try:
    x = int(input("First number: "))
    
    y = int(input("Second number: "))

except ValueError:
    print("Sorry! I need a number")

else:
    result = x+y
    print(f'Sum of x and y is {result}')