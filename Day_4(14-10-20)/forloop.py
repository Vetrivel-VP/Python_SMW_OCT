# This is my pen
# for str in "This is my pen":
#     print(str)

# for i in range(1, 5+1):
#     print(f'{i} : Your_Name')

sum = 0
for i in range(1, 5+1):
    sum = sum + i

print(f'The sum:{sum}')

# i=1, i<=5   1<=5
#         sum= 0 + 1 => 1     i = i + 1 => 2
# i = 2       2<=5
#         sum = 1 + 2 => 3    i=> 3
# i = 3       3<=5
#         sum = 3 + 3 => 6    i=> 4
# i = 4       4<=5
#         sum = 6 + 4 => 10   i => 5
# i = 5       5 <= 5
#         sum = 10 + 5 => 15  i=>6
# i = 6       6<=5        terminates the loop
#
#
# Factorial : Mathematics.
# 5! = 5 * 4 * 3 * 2 * 1            range(1, 5+1) = > 1,2,3,4,5


n = eval(input('Enter the factorial number:'))
fact = 1
for i in range(1, n+1):
    fact = fact * i
    # print(f' {fact} * {i}')

print(f'Factorial of {n} is {fact}')
