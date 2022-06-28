import re

string = 'search inside of this text please'

print('search' in string)  # True

print(re.search('this', string))  # returns a Match object, occurs at the
# index of 17 and ends at 21 - <re.Match object; span=(17, 21), match='this'>
