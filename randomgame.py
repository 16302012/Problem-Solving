# -*- coding: utf-8 -*-
"""
Created on Thu May 26 06:02:41 2022

@author: User
"""

from random import randint

#generate a num 1~10
answer = randint(1, 10)

#input from user?

#check the input is a number 1~10
while True:
    try:
        print(answer)
        guess = int(input('guess a number 1~10: '))
        
        if 0<guess<11:
            if guess == answer:
                print('You are a genius!')
                break
        else:
            print('Hey idiot! I said 1~10')
    except ValueError:
        print('Please enter a number')
        continue
#check if the num is right, otherwise ask again
