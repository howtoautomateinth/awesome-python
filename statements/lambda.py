from functools import reduce
def old_fashion():
    items = [1, 2, 3, 4, 5]
    squared = []
    for i in items:
        squared.append(i**2)
    print('squared value:',squared)

def map_lambda():
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, items))
    print('map example:',squared)

def filter_lambda():
    number_list = range(-5, 5)
    less_than_zero = list(filter(lambda x: x % 2 == 0, number_list))
    print('filter example:',less_than_zero)

def reduce_lambda():
    reduce_v = reduce((lambda x, y: x * y), [1, 2, 3, 4])
    print('reduce example:',reduce_v)

if __name__ == '__main__':
    old_fashion()
    map_lambda()
    filter_lambda()
    reduce_lambda()