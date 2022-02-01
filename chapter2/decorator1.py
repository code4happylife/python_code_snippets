def decorator_demo(func):
    def wrapper():
        print("This is a decorator message")
        func()
        print("This is also a decorator message")
    return wrapper

@decorator_demo
def hello():
    print("Hello world")

hello()
