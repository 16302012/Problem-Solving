# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:19:44 2022

@author: User
"""

"""
taking name from user and writing it to guest.txt file
"""
name = input("What's your name? ")

filename = 'guest.txt'
with open(filename,'w') as file:
    file.write(name)