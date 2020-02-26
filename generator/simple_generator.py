def create_data(n):
    for x in range(n):
        yield x**2

if __name__ == '__main__':
    for x in create_data(1000):
        print(x)