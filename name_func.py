# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:48:01 2022

@author: User
"""

def get_formatted_name(first, last, middle=''):
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()
