# -*- coding: utf-8 -*-
"""
Created on Fri May 13 18:26:21 2022

@author: User
"""
print("Printing current and previous number sum in a range(10)")
previous_num = 0

for i in range(1,11):
    x_sum = previous_num + i
    print(f"Current number {i} Previous number {previous_num} Sum: {previous_num+i}")
    previous_num=i