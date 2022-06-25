for _ in range(2): # not care about the number though
    print('hi')

# 10
# 8
# 6
# 4
# 2
for num in range(10, 0, -2):
    print(num)

for char in 'hellooo':
    print(char)

# 0 h
# 1 e
for i, char in enumerate('helloooo'):
    print(i, char)

for i, item in enumerate(['a', 'b', 'c']):
    print(i, item)

for i, item in enumerate(('a', 'b', 'c')):
    print(i, item)

obj = {
    'name': 'mike',
    'age': 30,
    'is_fun': True
}

for i, item in enumerate(obj.items()):
    print(i, item)

def get_index(num):
    li = range(1, 101, 2)

    for i, item in enumerate(li):
        if item == num:
            return i

    return -1

print(get_index(11))