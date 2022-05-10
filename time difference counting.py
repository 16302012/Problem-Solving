# -*- coding: utf-8 -*-
"""
Created on Tue May 10 21:09:33 2022

@author: User
"""
from time import time
def performance(func):
    def wrapper(*args,**kwargs):
        time1= time()
        result= func(*args,**kwargs)
        time2= time()
        print(f'took {time2-time1} seconds')
        return result
    return wrapper
@performance 
def long_time():
    for i in range(100000000):
        i*5
long_time() 