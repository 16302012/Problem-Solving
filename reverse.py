# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:40:31 2022

@author: User
"""

number = int(input('Give a number: '))
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end = "")