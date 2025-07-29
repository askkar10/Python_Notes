def decorator(func):
    def wrapper():
        print("Przed funkcją")
        func()
        print("Po funkcji")
    return wrapper
@decorator
def siema():
    print('siema')

siema()