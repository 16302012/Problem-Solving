# -*- coding: utf-8 -*-
"""
Created on Tue May 31 19:30:56 2022

@author: User
"""

import re
pattern = re.compile(r"[A-Za-z0-9$%#@]{8,}[0-9]")
password = 'eysyinas#&2732$$8'

a = pattern.fullmatch(password)
print(a)