import re

string = 'search this inside of this text please'

a = re.search('this', string)
print(a.span())  # (17, 21)
print(a.start())  # 17
print(a.end())  # 21
print(a.group())  # this
