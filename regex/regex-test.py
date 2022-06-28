import re

string = 'search this inside of this text please'

pattern = re.compile('this')

result = pattern.search(string)
print(result.group())  # this

b = pattern.findall(string)
print(b)  # ['this', 'this']

c = pattern.fullmatch(string)
print(c)  # None, the pattern shall be full match to the entire string

pattern = re.compile('search this')
d = pattern.match(string)  # the pattern need to match from the start
print(d)

pattern = re.compile(r'([a-zA-Z]).([a])')
e = pattern.search(string)
print(e.group())  # sea
print(e.group(1), e.group(2))  # s a
