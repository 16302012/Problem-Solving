# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:34:49 2022

@author: User
"""

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
result_list = []

for num in list1:
    if num % 2 != 0:
        result_list.append(num)
for num in list2:
    if num % 2 == 0:
        result_list.append(num)
print(list1)
print(list2)
print(result_list)        