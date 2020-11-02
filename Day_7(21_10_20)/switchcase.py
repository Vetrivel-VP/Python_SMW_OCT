"""
    1. Addition
    2. Subtraction
    3. Exit
    Select your choice : 1
                Addition of two numbers
        Enter the value of a,b : 5,5
        ANs : 5 + 5 = 10
        Do you want to continue. Press (Yes/No): Yes

    1. Addition
    2. Subtraction
    3. Exit
    Select your choice : 3
    Invalid Options
     Do you want to continue. Press (Yes/No): No
"""

import sys


def my_choices(ch):
    my_dict = {
        1: "Addition",
        2: "Subtraction",
        3: "Exit"
    }

    return my_dict.get(ch, "Invalid Option")


if __name__ == "__main__":
    restart = "yes"
    while restart[0] == 'y' or restart[0] == 'Y':
        print('1. Addition\n2. Subtraction\n3. Exit\n Select an option:')
        ch = eval(input())
        options = my_choices(ch)
        if options == "Addition":
            print('\t\tAddition of two numbers')
            a, b = eval(input('Enter the value of a,b:'))
            print(f'Ans: {a} + {b} = {a+b}')
            restart = input('Do you want to continue. Press (Yes/No):')

        elif options == "Subtraction":
            print('\t\tSubtraction of two numbers')
            a, b = eval(input('Enter the value of a,b:'))
            print(f'Ans: {a} - {b} = {a-b}')
            restart = input('Do you want to continue. Press (Yes/No):')

        elif options == "Exit":
            sys.exit()

        else:
            print(f'Warning: {options}')
            restart = input('Do you want to continue. Press (Yes/No):')
