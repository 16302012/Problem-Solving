# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 11:41:33 2022

@author: User
"""
"""
Write a Python program to create the combinations of 3 digit combo
"""
numbers = []
for num in range(1000):
    num = str(num).zfill(3)
print(num)
numbers.append(num)