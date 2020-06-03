# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:37:08 2020

@author: Babs
"""
exp1=[120,225,300,145,250]
exp2=[220,425,350,245,150]


def total_expense(expense_list):
    total=0
    for item in expense_list:
        total=total+item
    
    return total

first_exp=total_expense(exp1)
second_exp=total_expense(exp2)
    

"""reutrn total

first_exp=total_expense(exp1)
second_exp=total_expense(exp2)
"""
print("First expense is ",first_exp,"Second expense is ",second_exp)
