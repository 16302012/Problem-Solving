# -*- coding: utf-8 -*-
"""
Created on Mon May 30 20:41:29 2022

@author: User
"""

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = int(input("\nGive me a number: "))
        if x == 'q':
            break

        y = int(input("Give me another number: "))
        if y == 'q':
            break

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")