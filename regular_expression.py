# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:03:43 2022

@author: User
"""
import re 
pattern = re.compile('this') #compiled a pattern for search
string = 'search this inside of this text this please!'
#a = re.search('this',string)
a = pattern.search(string)
b = pattern.findall(string)
print(b)
print(a.span()) #tells us where it starts and where it ends
print(a.start()) #tells us when the string starts
print(a.end()) #tells us when the string ends
print(a.group()) #returns the match, useful for multiple searches
