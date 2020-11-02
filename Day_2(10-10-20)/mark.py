name = input('Enter the student name:')
m1, m2, m3, m4, m5 = eval(input('Enter the students mark:'))
tot = m1+m2+m3+m4+m5
average = tot / 5
print(f'Name : {name}, Total: {tot}, Average:{average}%')
