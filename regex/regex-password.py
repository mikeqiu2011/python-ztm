# at least 8 char long
# contain any sort letters, numbers, $%#@
import re

pattern = re.compile(r'(^[a-zA-Z\d$%#@]{8,}$)')

test = 'as$a12s'

result = pattern.fullmatch(test)

if result:
    print('password is compliant')
else:
    print('at least 8 char long, contain any sort letters, numbers, $%#@')
