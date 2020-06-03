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
   "babs":1,
   "sam":2,
   "akki":3,
   "nil":4,
   }

# Printing using key value
print("babs' Roll No=",d["babs"])

# using for loop
for i in d:
    print(i," roll no.=",d[i])

# using for loops  and tuple
for k,v in d.items():
    print(k," roll no=",v)
    
# checking key is present or not
    print("babs" in d)