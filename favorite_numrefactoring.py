# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:50:31 2022

@author: User
"""

import json
filename = 'favnum.json'
try:
    with open(filename) as file:
        number = json.load(file)
except FileNotFoundError:
    number = input("What's your favorite number? ")
    with open(filename,'w') as file:
        json.dump(number,file)
        print(f"We'll remember your favorite number {number}")
else:
    print(f"I know your favorite number! It's {number}")