# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 12:10:34 2022

@author: User
"""
"""
Write a Python program to count 
the number of each character of a given text of a text file
"""
import collections
import pprint
filename = 'text_files/test.txt'
with open(filename,'r') as file:
    count = collections.Counter(file.read().upper())
    value = pprint.pformat(count)
print(value)