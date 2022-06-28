import re

string = 'search this inside of this text please'

a = re.search('thIs', string)  # now a is None
print(a.group())  # will cause error
