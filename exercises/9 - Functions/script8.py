a = 10
print(a)
def f():
    global a
    a = 15
    return a
print(a)
f()
print(a)
a = 20
print(a)

def myfunc():
    x = 'Witam'
    def myfunc2():
        nonlocal x
        x = 'Hello'
    print(x)
    myfunc2()
    return x
print(myfunc())    