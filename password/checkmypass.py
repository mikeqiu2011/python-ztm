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
    first5_char, tail = sha1password[:5], sha1password[5:]
    print(first5_char, tail)

    resp = request_api_data(first5_char)
    return resp


def read_res(response):
    print(response.text)


query_char = '12345'
resp = pwned_api_check(query_char)
read_res(resp)
# request_api_data(query_char)
