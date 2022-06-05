# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 11:06:29 2022

@author: User
"""

num_list = [1,5,7,3,8,34,21,65,9,32,54,97,22,13,53]

def print_every_3rd(num_list):
    for i in num_list[0:14:4]:
        print(i)
        
print_every_3rd(num_list)