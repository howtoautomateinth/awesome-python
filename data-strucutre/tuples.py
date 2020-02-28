#!/usr/bin/python
# -*- coding: utf-8 -*-

# passing object around the system without reassignment

# different from list
# - immutable
# - init with '()' instead of '[]'
mytuples = (1,2,2,3)
mylist = [1,2,3]
print(type(mytuples))
print(type(mylist))

# count how many value 
print(mytuples.count(2))
# first time apeear 2
print(mytuples.index(2))

# reassign
mylist[0] = 'new data'
mytuples[0] = 'new data'