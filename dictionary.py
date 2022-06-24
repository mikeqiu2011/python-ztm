dictionary = {
    'a': 1,  # a and b are not adjacent to each other like list
    'b': 2,
    'b': 3,
    'x': [1,2],
    'hi': True,
    123: [1,2,3],
    #[100]: True  # unhashable type: 'list', list is NOT immutable, which cannot be hashed, thus cannot act like a key
}

print(dictionary['a']) #1
print(dictionary['x'][0]) #1
print(dictionary[123]) # [1,2,3]
print(dictionary['b']) # 3, the duplicated key will overwrite previous key's value
