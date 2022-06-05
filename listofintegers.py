# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:58:50 2022

@author: User
"""

"""
Write a Python program find a list of integers with exactly 
two occurrences of nineteen and at least three occurrences of five
"""
def test(num):
    return num.count(19)==2 and num.count(5)>=3
num = [19, 19, 15, 5, 3, 5, 5, 2]
print(f"Input: {num}")
print(f'Output: {test(num)}')

num = [19, 15, 15, 5, 3, 3, 5, 2]
print(f"Input: {num}")
print(f'Output: {test(num)}')

num = [19, 19, 5, 5, 5, 5, 5]
print(f"Input: {num}")
print(f'Output: {test(num)}')

