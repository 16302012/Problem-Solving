# -*- coding: utf-8 -*-
"""
Created on Tue May 31 18:37:51 2022

@author: User
"""

import re
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'
a = pattern.match(string)
print(a)