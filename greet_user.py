# -*- coding: utf-8 -*-
"""
Created on Tue May 31 13:45:27 2022

@author: User
"""

import json 
filename = 'username.json'
with open('text_files/filename') as file:
    username = json.load(file)
    print(f"Welcome back {username}")