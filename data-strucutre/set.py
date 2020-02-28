#!/usr/bin/python
# -*- coding: utf-8 -*-


# Sets are mutable. But since they are unordered, indexing have no meaning.
# there is no way of determining which item will be popped

# set initial way
myword = set('Hello World')
mybasket = {'orange', 'apple', 'pear', 'orange', 'banana', 'apple'}
mynumber = {500,99,900,2,34,5,77,8}

# unorder word
print(myword)

# unordered collection with no duplicate elements
print(mybasket)

# adding second time
# show no duplicate 
mynumber.add(77)
print(mynumber)

# cast list to set
mylist = [5,2,2,2,3,1,1,1,3]
print(set(mylist))