def fibonacci_generator(n):
    a = 1 
    b = 1
    for x in range(n):
        yield a
        a,b = b,a+b

if __name__ == '__main__':
    for x in fibonacci_generator(10):
        print(x)