#!/usr/bin/python
# -*- coding: utf-8 -*-

def commonappendlist():
    mylist = []
    mystring = 'Hello World'
    for letter in mystring:
        mylist.append(letter)
    return mylist

def comprehensionlist():
    mylist = []
    mystring = 'Hello World'
    # `letter` temp variable name that will iterate from iterable object
    # have to match each other
    mylist = [letter for letter in mystring]
    return mylist

def comprehensionlist_if():
    mylist = []
    mystring = 'Hello World'
    mylist = [letter if letter != 'o' else 'x' for letter in mystring]
    return mylist

def comprehensionlist_nestedloop():
    mylist = []
    # innner to outter loop
    # eqivalent to 
    # for x in [2,4,6]:
    #   for y in [1,10,100]:
    #      mylist.append(x*y)
    mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
    return mylist

if __name__ == '__main__':
    print(commonappendlist())
    print(comprehensionlist())
    print(comprehensionlist_if())
    print(comprehensionlist_nestedloop())