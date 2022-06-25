# dictionary = {
#     'a': 1,  # a and b are not adjacent to each other like list
#     'b': 2,
#     'b': 3,
#     'x': [1,2],
#     'hi': True,
#     123: [1,2,3],
#     #[100]: True  # unhashable type: 'list', list is NOT immutable, which cannot be hashed, thus cannot act like a key
# }
#
# print(dictionary['a']) #1
# print(dictionary['x'][0]) #1
# print(dictionary[123]) # [1,2,3]
# print(dictionary['b']) # 3, the duplicated key will overwrite previous key's value

dictionary = {
    'basket': [1,2,3],
    'greet': 'hello'
}
# print(dictionary['age']) # KeyError: 'age'
print(dictionary.get('age')) # None, program does not prompt error, continue execution
print(dictionary.get('age', 30)) # 30 as default value if key not exist

user = dict(name='mike')
print(user) #{'name': 'mike'}

print('basket' in dictionary) # True
print('basket' in dictionary.keys()) # True
print('hello' in dictionary.values()) # True

print(dictionary.items()) # dict_items([('basket', [1, 2, 3]), ('greet', 'hello')])



dictionary2 = dictionary.copy()
dictionary.clear()
print(dictionary) # {}

print(dictionary2) # {'basket': [1, 2, 3], 'greet': 'hello'}

print(dictionary2.pop('greet')) # hello
print(dictionary2) # {'basket': [1, 2, 3]}

dictionary2.update({'age': 55}) # if not exist key, it will insert new record
dictionary2.update({
    'basket': 'banana'
})
print(dictionary2) # {'basket': 'banana', 'age': 55}

