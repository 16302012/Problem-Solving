# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:17:15 2022

@author: User
"""

"""Write all content of test.txt file into a 
newfile.txt by skipping line number 5
"""
#read test.txt
with open('text_files/test.txt') as file:
    lines = file.readlines()
    
#create a new file to write
with open('text_files/newfile.txt','w') as file:
    count = 0
    for line in lines:
        #skip 5th line
        if count == 4:
            count+=1
            continue
        else:
            #write current line
            file.write(line)
        #in each iteration reduce the count
        count+=1