# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:47:31 2022

@author: User
"""

import json

filename = 'favnum.json'
with open(filename) as file:
    number = json.load(file)
print(f"I know your favorite number! It's {number}")