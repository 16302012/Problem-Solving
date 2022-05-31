# -*- coding: utf-8 -*-
"""
Created on Tue May 31 21:01:52 2022

@author: User
"""

def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))