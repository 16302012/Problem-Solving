# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 22:07:17 2022

@author: User
"""

import unittest
from survey import AnonymousSurvey

class TestAnonmyousSurvey(unittest.TestCase):
    def test_store_single_response(self):
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
        
unittest.main()