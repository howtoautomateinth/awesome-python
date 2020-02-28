#!/usr/bin/python
# -*- coding: utf-8 -*-

def forloop():
    # traditionally for-loop
    for x in range(0, 3):
        print('We\'re on time %d' % (x))

def whileloop():
    x = 0
    # base on condition while
    while (x<15):
        print('To infinity and beyond! We\'re getting close, on %d now!' % (x))
        x += 1

def forelse():
    # after conditon will execute else block 
    for x in range(3):
        print(x)
    else:
        print('Final x = %d' % (x))

def forwithiterable():
    collection = ['hey', 5, 'd']
    for x in collection:
        print(x)

def loppenumerate():
    word = 'abcde'
    # instead of create running index use enumerate instead 
    for index,letter in enumerate(word):
        print(index)
        print(letter)

def ziplist():
    # zip n lists into one list
    # will zip only shortest list
    number_list = [1,2,3,5,6,7,8,9]
    string_list = ['a','b','c']
    for n,s in zip(number_list,string_list):
        print(n)
        print(s)

if __name__ == '__main__':
    forloop()
    print('\n')
    whileloop()
    print('\n')
    forelse()
    print('\n')
    forwithiterable()
    print('\n')
    loppenumerate()
    print('\n')
    ziplist()