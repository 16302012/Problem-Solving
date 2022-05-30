# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:13:21 2022

@author: User
"""

filename = 'alice.txt'

try:
    with open(filename) as file:
        content = file.read()
except FileNotFoundError:
    print(f'Sorry! the file {filename} does not exist')