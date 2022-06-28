# at least 8 char long
# contain any sort letters, numbers, $%#@
import re

pattern = re.compile(r'(^[a-zA-Z\d$%#@]{7,}\d$)')

test = 'asasaas$a12s1'

result = pattern.fullmatch(test)

if result:
    print('password is compliant')
else:
    print('at least 8 char long, contain any sort letters, numbers, $%#@')
