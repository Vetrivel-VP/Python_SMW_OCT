class Myclass:
    pass


class Person:                       # parent classs
    def __init__(self, name, age):
        self.fname = name
        self.page = age

    def myfunc(self):
        print(f"Hello my name is {self.fname} and my age is {self.page}")


class Student(Person):  # child Class
    def __init__(self, name, age, year):
        self.year = year
        super().__init__(name, age)

    def graduation(self):
        print(f'{self.fname} age is {self.page}, he graduated in the year {self.year}')


if __name__ == "__main__":
    p1 = Student("John", 21, 2016)

    p1.graduation()
