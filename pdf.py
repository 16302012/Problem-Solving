# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:04:13 2022

@author: User
"""

import PyPDF2

with open('dummy.pdf.pdf','rb') as file:  #'rb': read binary
    reader = PyPDF2.PdfFileReader(file)
    print(reader.getPage(0))