class CustomHTAError(Exception):
    pass

def sum_if_positive(a,b):
    try:
        if (a > 0 ) and (b > 0):
            return print('sum value is',a+b)
        else:
            raise CustomHTAError('Negative Value Is Not Acceptable')
    except CustomHTAError as errorValue:
        print(errorValue)

sum_if_positive(-1,2)