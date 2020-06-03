# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:01:16 2020

@author: Babs
"""

class Employee:
    def __init__(self,n,o):
        self.name=n
        self.occupation=o
    def work(self):
        if(self.occupation=="Teacher"):
            print(self.name+" is a "+self.occupation+" Payment is $35000")
        elif (self.occupation=="Driver"):
            print(self.name+" is a "+self.occupation+" Payment is $20000")
        else:
            print(self.name+" is a "+self.occupation+" Payment is $20000 to $50000")

ee= Employee("a","Driver")
ee.occupation="Teacher"
ee.work()
