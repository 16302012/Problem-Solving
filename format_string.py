# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 19:35:24 2022

@author: User
"""

quantity = 3
totalMoney = 1000
price = 450

string = "I have {1} dollars so I can buy {1} football for {2:.2f} dollars"
print(string.format(quantity, totalMoney, price))