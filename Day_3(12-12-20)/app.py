# age = eval(input('Enter the candidate age:'))
# if age >= 18:
#     print(f'The candidate is eligible to vote.')
# else:
#     print(f'The candidate is Not eligible to vote.')

# # Output:
# #     Enter a number: 24
# #     24 is an even number

# #     Enter a number: 15
# #     15 is an Not an even number

# #     Read a number
# #     Divide that number by 2
# #     Check the reminder is equal to 0.
# #     If equals to 0 then Print num is an even number
# #     else Print num is not an even number


name = input('Enter the student name:')
m1, m2, m3, m4, m5 = eval(input('Enter the marks following m1,m2,m3,m4,m5:'))
total = m1+m2+m3+m4+m5
avg = total / 5
if avg >= 35 and avg <= 50:
    grade = 'C Grade'
elif avg >= 51 and avg <= 65:
    grade = 'b Grade'
elif avg >= 66 and avg <= 75:
    grade = 'A Grade'
elif avg >= 76 and avg <= 100:
    grade = 'A+'
else:
    grade = 'Fail'

print(f'Name: {name} Total: {total} Average:{avg} Grade: {grade}')
