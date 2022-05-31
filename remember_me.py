# -*- coding: utf-8 -*-
"""
Created on Tue May 31 17:12:27 2022

@author: User
"""

import json
filename = 'username.json'

try:
    with open('text_files/filename') as file:
        username = json.load(file)

except FileNotFoundError:
    username = input("What is your name? ")
    with open('text_files/filename','w') as file:
        json.dump(username, file)
        print(f"We'll remember you when you come back {username}!!")
        
else:
    print(f"Welcome back {username}")