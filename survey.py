# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 21:52:31 2022

@author: User
"""

class AnonymousSurvey():
    def __init__(self,question):
        self.question = question
        self.responses = []
    def show_question(self):
        print(question)
    def store_response(self, new_response):
        self.responses.append(new_response)
    def show_results(self):
        print("Survey results:")
        for response in responses:
            print('- ' + response)