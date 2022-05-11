# -*- coding: utf-8 -*-
"""
Created on Wed May 11 16:53:24 2022

@author: User
"""

while True:
    try:
        age=int(input('What is your age? '))
        10/age
        raise Exception('hey cut it out')
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Please enter age higher than zero')
        break
    else:
        print('Thankyou!')
    finally:
        print("ok I'm finally done")
    print("can you hear me?")