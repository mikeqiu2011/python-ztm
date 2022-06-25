# iterable - list, dictionary, tuple, set, string
# they can be iterated - one by one to check each item in the collection

user = {
    'name': 'mike',
    'age': 30,
    'can_swim': False
}

# name
# age
# can_swim
for key in user:
    print(key)

# ('name', 'mike')
# ('age', 30)
# ('can_swim', False)
for item in user.items():
    print(item)

for value in user.values():
    print(value)

for item in user.items():
    key, value = item
    print(key, value)

for key, value in user.items():
    print(key, value)