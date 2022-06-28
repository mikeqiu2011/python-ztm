from collections import Counter, defaultdict, OrderedDict

# count duplicated items, to be optimized
# li = [1,2,4,5,6,7,7,7,8,6,2]
# print(Counter(li)) #
#
# sentence = 'hi hi hi python is good'
# print(Counter(sentence)) # Counter({' ': 5, 'h': 4, 'i': 4, 'o': 3, 'p': 1, 'y': 1, 't': 1, 'n': 1, 's': 1, 'g': 1, 'd': 1})


# my_dict = defaultdict(lambda: 5, {
#     'a': 1,
#     'b': 2,
# })
# print(my_dict['a'])
# print(my_dict['c']) # now instead of keyError, it will return default value of 5

d = {}
d['a'] = 1
d['b'] = 2

d2 = {}
d2['b'] = 2
d2['a'] = 1

print(d2 == d)  # True

d3 = OrderedDict()
d3['a'] = 1
d3['b'] = 2

d4 = OrderedDict()
d4['b'] = 2
d4['a'] = 1

print(d4 == d3)  # False
