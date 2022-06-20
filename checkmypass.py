# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 19:27:21 2022

@author: User
"""

import requests
url = 'https://api.pwnedpasswords.com/range/'+'CBFDA'
res = requests.get(url)
print(res)