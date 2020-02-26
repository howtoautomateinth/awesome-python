class TestCall:
    def __init__(self):
        print('init')

    def __call__(self):
        print('call')

if __name__ == '__main__':
    a = TestCall()
    a()