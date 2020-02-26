# Decorators Python

Decorate function with an already existing function

> All about scope and passing function

- nested function
- function as argument

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

# Syntactic Sugar - use @ operator and place on top of the original function
@my_decorator
def say_whee():
    print("Whee!")
```
