# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 16:35:25 2022

@author: User
"""

import unittest
import main2

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = main2.do_stuff(test_param)
        self.assertTrue(result, 20)