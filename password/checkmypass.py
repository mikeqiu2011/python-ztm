import requests
import hashlib


# https://passwordsgenerator.net/sha1-hash-generator/

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError(f'Error fetching: {resp.status_code}, check the '
                           f'api and try again')

    return resp


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(sha1password)
    
    return sha1password


query_char = '12345'
pwned_api_check(query_char)
# request_api_data(query_char)
