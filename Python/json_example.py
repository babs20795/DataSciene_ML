# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 13:52:47 2020

@author: Babs
"""

import json

book={}

book["Alchemist"]={
                'Author':'a',
                'price':100
        }

book["Word power made easy"]={
                'Author':'b',
                'price':200
        }

s=json.dumps(book)

f=open("json_data.txt","w+")
f.write(s)
f.close()

f=open("json_data.txt","r")
data=f.read()
book=json.loads(data)
print(book["Alchemist"]["price"])

for bookname in book:
    print(book[bookname])
f.close()