def my_decorator(func):
    def wrapper():
        print("before the function is called.")
        func()
        print("after the function is called.")
    return wrapper

@my_decorator
def say_hi_HTA_with_syntax():
    print("Hi! HTA with_syntax")

def say_hi_HTA_without_syntax():
    print('Hi! HTA without_syntax')

if __name__ == '__main__':
    say_hi_HTA_with_syntax()
    print('-----=-----')
    say_hi_HTA_without_syntax = my_decorator(say_hi_HTA_without_syntax)
    say_hi_HTA_without_syntax()