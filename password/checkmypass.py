import requests

# https://passwordsgenerator.net/sha1-hash-generator/

url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'

resp = requests.get(url)
print(resp)
