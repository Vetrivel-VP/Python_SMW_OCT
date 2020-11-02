thisset = {'apple', 'banana', 'orange'}
for name in thisset:
    print(name)

print('apple' in thisset)

# add() : add one more element inside the set.
thisset.add('cherry')
print(thisset)

# update(): to add more than one element inside the set by using update().

thisset.update(['jack fruit', 'Peaches', 'Pine apple'])
print(thisset)

# len()
print(len(thisset))

# remove(): By looking the exact matching value.
thisset.discard('cRACK')
print(thisset)

# discard() : By looking the exact matching value. It doesn't raise an error if your element is not
# inside the set

# clear() : clears the entire set
# del : Keyword removes the complete set

# joining two sets: Union()
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)
