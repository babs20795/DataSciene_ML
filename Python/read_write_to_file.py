# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 11:58:45 2020

@author: Babs
"""
"""
File in Writing appending mode to write the data
f=open("F:\\Data Science\\Practice\\First_Python\\abc.txt","a")
f.write("\nFrom Gad")
f.close()
"""
import time

f=open("F:\\Data Science\\Practice\\First_Python\\abc.txt","r")
for line in f.readlines():
    print(line)
    time.sleep(2) 
f.close()

# it automatically closes a files
"""
with open("F:\\Data Science\\Practice\\First_Python\\abc.txt","r") as f:
    for line in f.readlines():
    print(line)
    time.sleep(2) 

    """
