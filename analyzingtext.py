# -*- coding: utf-8 -*-
"""
Created on Mon May 30 18:17:06 2022

@author: User
"""

filename = 'alice.txt'

try:
    with open(filename) as file:
        content = file.read()
except FileNotFoundError:
    print(f'Sorry! the file {filename} does not exist')
else:
    words = content.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words")