# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:52:37 2022

@author: User
"""

filename = 'programming.txt'
with open(filename, '+r') as file:
    file.write("I hate programming but I like python.\n")
    file.write("I love working with large datasets.\n")

