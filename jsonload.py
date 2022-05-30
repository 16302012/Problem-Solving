# -*- coding: utf-8 -*-
"""
Created on Mon May 30 21:37:06 2022

@author: User
"""

import json

filename = 'numbers.json'
with open(filename) as file:
    numbers = json.load(file)
print(numbers)