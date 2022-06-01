# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 16:24:39 2022

@author: User
"""

def palindrome(num):
    print(f'original number: {num}')
    original_num = num
    
    reverse_num = 0
    while num > 0:
        remainder = num % 10
        reverse_num = (reverse_num*10) + remainder
        num = num//10
        
    if original_num == reverse_num :
        print("Yes. Given number is a palindrome")
    else:
        print("No. Given number is not a palindrome")
        
palindrome(121)
palindrome(1551)
palindrome(124)