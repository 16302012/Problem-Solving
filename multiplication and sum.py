# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:11:45 2022

@author: User
"""

def multiplication_or_sum(num1,num2):
    product = num1*num2
    if product <= 1000:
        return product
    else:
        return num1+num2
result = multiplication_or_sum(20, 30)
print(f'The result is {result}')
result = multiplication_or_sum(40, 30)
print(f'The result is {result}')