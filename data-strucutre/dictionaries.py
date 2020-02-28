#!/usr/bin/python
# -*- coding: utf-8 -*-

# simple dictionary
mybasket = {'apple':2.99,'orange':1.99,'milk':5.8}    
print(mybasket['apple'])

# dictionary with list inside
mynestedbasket = {'apple':2.99,'orange':1.99,'milk':['chocolate','stawbery']}    
print(mynestedbasket['milk'][1].upper())

# append more key
mybasket['pizza'] = 4.5
print(mybasket)

# get only keys
print(mybasket.keys())
# get only values
print(mybasket.values())
# get pair values
print(mybasket.items())