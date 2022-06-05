# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 10:56:33 2022

@author: User
"""

def distinct_num(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False
print(distinct_num([1,5,3,7,4]))
print(distinct_num([1,4,3,7,5,3,2]))