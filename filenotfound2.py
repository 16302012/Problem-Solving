# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:44:36 2022

@author: User
"""

filenames = ['cats.txt','dogs.txt']

for filename in filenames:
    
    try:
        with open(filename) as file:
            content = file.read()
            
    except FileNotFoundError:
        pass
    else:
        print(f'\nReading file: {filename}')
        print(content)