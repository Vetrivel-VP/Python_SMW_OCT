# *                         0 + 1
# * *                       1 + 1
# * * *                     2 + 1
# * * * *                   3 + 1
# * * * * *                 4 + 1

rows = 5
for i in range(rows):  # rows = 0,1,2,3,4
    for j in range(0, i+1):
        print("*", end='')

    print("\r")

    # Escape Sequence : \n : New Line, \t : Tab Space, \r : New Row, \b : Break
