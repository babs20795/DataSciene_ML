# -*- coding: utf-8 -*-
"""
Created on Sat May 30 15:10:50 2020

@author: Babs
"""

import numpy as np

a = np.array([1, 2, 3, 4, 5])

print("Array = ",a)

# Third Argument is for gap so output= 1,3,5,7,9
a = np.arange(1, 10, 2)

print ("Array =",a)

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])
print("Array a = ",a ,"Array b = ",b)

print("Array Addition = ",(a+b))
print("Array Subtraction(b-a) = ",(b-a))
print("Array Multiplication = ",(a*b))
print("Array Division = ",(b/a))
