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
    return get_password_leaks_count(resp, tail)


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    # print(hashes)
    for hash, count in hashes:
        print(hash, count)


query_char = '12345'
resp = pwned_api_check(query_char)
get_password_leaks_count(resp, '12345')
# request_api_data(query_char)
