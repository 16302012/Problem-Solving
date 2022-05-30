# -*- coding: utf-8 -*-
"""
Created on Mon May 30 11:31:47 2022

@author: User
"""

filename = 'test.txt'
with open(filename) as file:
     lines = file.readlines()
     
pi_string = ""
for line in lines:
    pi_string += line.strip()
    
#print(pi_string[:54] + '...')
#print(len(pi_string))
"""
checking if my bday is contained in Pi

"""
bday = input("Enter your birthday in the form mmddyy: ")
if bday in pi_string:
    print("Yaaay...your birthday appears in the first million digits of pi!")
    
else:
    print("Your birthday does not appear in the first million digits of pi. Sorry")