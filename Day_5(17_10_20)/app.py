n = eval(input('Enter the number of students:'))
students = []
for i in range(n):
    name = input('Enter the student name:')
    m1, m2, m3, m4, m5 = eval(input('Enter the Students mark:'))
    total = m1 + m2 + m3 + m4 + m5
    avg = total / 5
    st = [i+1, name, total, avg]
    students.append(st)

print(students)
