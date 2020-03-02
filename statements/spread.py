# unpacking like JS
# const oldObject = { hello: 'world', foo: 'bar' }
# const newObject = { ...oldObject, foo: 'baz' }
# using * and ** 
def spread():
    old_list = [1, 2, 3]
    new_list = [*old_list, 4, 5]
    print('spread example:',new_list)

def spread_kw():
    eatables = {
        'mango': '1$',
        'banana': '0.5$'
    }
    drinks = {
        'water': '0.3$',
        'wine': {
            'white': '2$',
            'red': '1.5$'
        }
    }
    menu = {
        **eatables,
        **drinks
    }
    print(menu)

if __name__ == '__main__':
    spread()
    spread_kw()