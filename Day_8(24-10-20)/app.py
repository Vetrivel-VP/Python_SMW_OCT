def x(a, b): return a * b


def addition(a, b, c): return a+b+c


def myfunc(n):
    return lambda a: a * n


x = myfunc(2)       # parameter of normal function n

print(x(2))         # parameter of your lambda function a
