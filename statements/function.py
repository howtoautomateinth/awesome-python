from functools import reduce
def plus(x,y,z):
    print('sum:',x+y+z)

# *args (variable number of non keyword arguments to function)
def pluser(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print('type of *num:', type(num))
    print('sum all:', sum)

def pluser_ls(*ls):
    print('type of *ls:', type(ls))
    print('*ls value', ls)
    for ldata in ls:
        print('Value of list',reduce(lambda x, y: x + y,ldata))

# **kwargs (The arguments are passed as a dictionary and these arguments make a dictionary inside function)
def pluser_kw(**data):
    print('\nData type of argument:',type(data))

    for key, value in data.items():
        print('{} is {}'.format(key,value))

if __name__ == '__main__':
    plus(10,12,13)
    pluser(5,6,7,8,9,10,11,12)
    pluser_ls([1,2,34],[55,6,7],[8,2,34],[1,20,34])
    pluser_kw(FirstData="First", SecondData="Second", LastData='Last')