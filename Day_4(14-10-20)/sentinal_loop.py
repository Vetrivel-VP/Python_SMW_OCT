restart = "yes"
while restart == "yes" or restart == "YES" or restart == "Yes":
    a, b = eval(input('Enter the value of a,b:'))
    c = a + b
    print(f'{a} + {b} = {c}')
    restart = input('Do you want to continue. Pres(Yes/No):')
