
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 17:49:10 2022

@author: User
"""

import unittest
from name_func import *

class NameTest(unittest.TestCase):
    def test_name(self):
        name = get_formatted_name('raisa','azad')
        self.assertTrue(name, 'Raisa Azad')
unittest.main()