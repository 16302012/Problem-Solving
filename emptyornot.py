# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:43:30 2022

@author: User
"""

import os
size = os.stat("text_files/test.txt").st_size
if size == 0:
    print('file is empty')
else:
    print('file has contents')