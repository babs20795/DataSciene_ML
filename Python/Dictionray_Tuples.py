# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 13:16:09 2020

@author: Babs
"""
# Tuple= immutable
a=(10,"a",20,"b",30,"c",40,"d")

for i in a:
    print(i)
    
# Dictionary =mutable
    
d={
   "Ace":1,
   "Jenette":2,
   "Amen":3,
   "Alex":4,
   }

# Printing using key value
print("Jenette's Roll No = ",d["Jenette"])

# using for loop
for i in d:
    print(i," roll no.=",d[i])

# using for loops  and tuple
for k,v in d.items():
    print(k," roll no=",v)
    
# checking key is present or not
    print("Ace" in d)