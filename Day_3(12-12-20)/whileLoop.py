i = 1
sum = 0
while i <= 5:
    sum = sum + i
    i = i + 1

print(f'Sum = {sum} ')


# i = 0       i < 5   =>  0 < 5
#     Your Name       i+1 => 0 + 1 = 1
# i = 1       i < 5 => 1 < 5
#     Your Name       => i + 1 = > 1 + 1 => 2
# i = 2       i < 5 => 2 < 5
#     Your Name      => 2 + 1 => 3
# i = 3       i < 5 => 3 < 5
#     Your Name      => 3 + 1 => 4
# i = 4       i < 5 => 4 < 5
#     Your Name      => 4 + 1 => 5
# i = 5   i < 5 => 5 < 5

# 1 + 2 + 3 + 4 + 5 = 15


# i = 1, i <= 5 1 <= 5
# sum = sum + i
# = 0 + 1
# = 1         1 = >2

# i = 2   2 <= 5
# = 1 + 2
# = 3         2 = > 3
# i = 3    3 <= 5
# = 3 + 3
# = 6         3 = > 4
# i = 4    4 <= 5
# = 6 + 4
# = 10        4 = >5
# i = 5   5 <= 5
# =10 + 5
# = 15         5 = >6
# i = 6   6 <= 5
