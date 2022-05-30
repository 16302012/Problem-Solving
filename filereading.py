# -*- coding: utf-8 -*-
"""
Created on Sat May 28 21:00:30 2022

@author: User
"""
file_path = 'C:/Users/User/Desktop/test.txt'
with open(file_path) as file:
    for line in file:
        print(line)
    