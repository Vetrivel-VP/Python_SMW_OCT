# thidict = {
#     'brand': 'BMW',
#     'MOdel': 'M8 GT',
#     'Year': 2020
# }
# print(thidict['brand'])

# # get()
# x = thidict.get('brand')
# print(x)


# thidict['Year'] = 2019
# print(thidict)

# for x in thidict:
#     print(thidict[x])


# # values():: Returns the values of keys.
# for x in thidict.values():
#     print(x)

# # items() : Returns the key and the value
# for key, value in thidict.items():
#     print(f'Key : {key}, Value : {value}')


# thidict['color'] = 'Black'
# print(thidict)


# #pop(), popitem(), clear()
# # pop(): Removes the specified key name
# # popitem() : Removes the last inserted item
# # clear(): Completey empty the dictionary
# # del : keyword deletes entire dictionary.

# thidict.pop('Year')
# print(thidict)

# thidict.popitem()
# print(thidict)

# thidict.clear()
# print(thidict)


cars = {
    "bmw": {
        'model': 'M5',
        'color': 'black'
    },
    "audi": {
        'model': 'A4',
        'color': 'White'
    }
}

car1 = {
    'model': 'M5',
    'color': 'black'
}

car2 = {
    'model': 'A4',
    'color': 'White'
}

cars1 = {
    'car1': car1,
    'car2': car2
}

print(cars1)
