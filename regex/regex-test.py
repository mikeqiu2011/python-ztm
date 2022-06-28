import re

string = 'search this inside of this text please'

pattern = re.compile('this')

result = pattern.search(string)
print(result.group())  # this

b = pattern.findall(string)
print(b)  # ['this', 'this']