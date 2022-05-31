# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:43:09 2022

@author: User
"""

import json
number = input("What's your favorite number? ")

filename = 'favnum.json'
with open(filename,'w') as file:
    json.dump(number,file)
