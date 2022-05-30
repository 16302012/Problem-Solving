# -*- coding: utf-8 -*-
"""
Created on Mon May 30 12:41:54 2022

@author: User
"""

filename = 'guest_book.txt'

print("Enter 'quit' to discontinue")

while True:
    name = input('\nWhat is your name? ')
    if name == 'quit':
        break
    else:
        with open(filename,'a') as file:
            file.write(f'{name}\n')
        print(f'Hi {name}, you have been added to the guest book')