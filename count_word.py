# -*- coding: utf-8 -*-
"""
Created on Mon May 30 19:19:07 2022

@author: User
"""

def count_words(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
    # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
filename = 'alice.txt'
count_words(filename)