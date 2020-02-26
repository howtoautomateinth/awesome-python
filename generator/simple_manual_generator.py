def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n


if __name__ == '__main__':
    a = my_gen()
    # return generator obj.
    print(a)
    print(next(a))
    # it will resume their execution and state around the last point of value
    print(next(a))
    # and go to next yield
    print(next(a))
    # and when no more yiled it will do a 'StopIteration'
    print(next(a))