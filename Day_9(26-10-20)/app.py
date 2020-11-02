def addition(a, b, c=0):
    print(f'Sum = {a+b+c}')


class FirstClass:
    def run(self):
        print(f'I am inside the Firstclass run method:')


class SecondClass(FirstClass):
    def run(self):
        print('I am inside the SecondClass run method')


class Person:
    def __init__(self):
        self.fname = "John"
        self.lname = "Smith"
        self.__year = 2019

    def run(self):
        print(
            f'First Name: {self.fname}, Last Name : {self.lname}, Year: {self.__year}')


if __name__ == "__main__":
    p = Person()

    p.run()
