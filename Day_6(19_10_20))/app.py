thistuple = ('apple', 'orange', 'banana')
# tuple with single element

singletuple = ('cherry',)
# type()
print(type(singletuple))

# remove a single element
# del is the keyword used to delete it completely
del singletuple

# list() : Contructor which helps you to convert a tuple or a set or string to list

thislist = list(thistuple)
thislist[0] = "APPLE"
print(thislist)

# tuple() : to covert anything to a tuple

thistuple = tuple(thislist)
print(thistuple)
