def hello():
    print('Hello world')


def addition():
    a, b = eval(input('ENter the value of a,b:'))
    c = a + b
    print(f'Ans: {c}')


def add(a, b):
    c = a + b
    #c = 10
    print(f'Ans: {c}')


if __name__ == "__main__":
    add(5, 6)
