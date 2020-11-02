thislist = ['apple', 'orange', 'banana']
thislist[0] = "Apple"
print(thislist)

# appened()
# thislist.append('Cherry')
# print(thislist)

# insert()
# Add an element in a specified index number
# thislist.insert(1, 'Jack Fruit')
# print(thislist)

# Remove an element:
""" 
    remove()    : Remove method removes the sepcified string object.
    pop()       : It removes the element by the index number. By default it removes the last element of your list
    del         : Del is a keyword. 
"""
# thislist.remove('orange')
# thislist.pop(0)
# del thislist
# print(thislist)

# clear() : Remove all the elements in the list.

# thislist.clear()
# print(thislist)
# copy() : From one list to another
# mylist = thislist.copy()
# print(f'Mulist {mylist}')

# Join List together

mylist = [50, 20, 30]
# + Operator

# final_lsit = thislist + mylist
# print(final_lsit)

# appened() with for loop
# for x in mylist:
#     thislist.append(x)
# print(thislist)

# extend()
# thislist.extend(mylist)
print(thislist)

# sort()
thislist.sort()
print(thislist)
