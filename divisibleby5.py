# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:07:15 2022

@author: User
"""

num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print('Divisible by 5:')
for num in num_list:
    if num % 5 == 0:
        print(num)