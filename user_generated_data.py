# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:34:00 2022

@author: User
"""

import json
username = input("What is your name? ")

filename = 'username.json'
with open('text_files/filename','w') as file:
    json.dump(username, file)
    print(f"We'll remember you when you come back {username}!!")