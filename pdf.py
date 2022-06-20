# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 20:04:13 2022

@author: User
"""

import PyPDF2
import sys

inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merger.append(pdf)
    merger.write('super_pdf')
        
pdf_merger(inputs)
#with open('dummy.pdf.pdf','rb') as file:  #'rb': read binary
#    reader = PyPDF2.PdfFileReader(file)
#    print(reader.getPage(0))