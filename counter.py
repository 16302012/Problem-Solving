# -*- coding: utf-8 -*-
"""
Created on Thu May 26 07:27:40 2022

@author: User
"""

from collections import Counter, defaultdict, OrderedDict

list = [1,4,2,5,3,8,3]
sentence = ("oh man i am sleepy")
print(Counter(list))
print(Counter(sentence))

dictionary = defaultdict(lambda:5,{'a':1,'b':2})
print(dictionary['d'])

d = OrderedDict()

d['a']= 1
d['b']= 2

d2= OrderedDict()
d2['a']=1
d2['b']=2

print(d2==d)