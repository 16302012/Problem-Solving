# -*- coding: utf-8 -*-
"""
Created on Mon May 30 21:07:09 2022

@author: User
"""

import json

numbers = [2,5,6,3,8,1]
filename = 'numbers.json'
with open(filename,'w') as file:
    json.dump(numbers, file)