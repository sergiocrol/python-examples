import requests
import hashlib
import sys

# With this api, the password we're sending in the request must be SHA1 hashed
# But since using just SHA1 is not totally secure, it also uses a technique called "K anonymity", this allow the
# the companies to track someone data without knowing who they are. This works giving only the first five characters of
# our hashed password. The API will return ALL the leaked passwords starting with those five characters (so they will
# never know the password we are sending), and we're gonna take care of them in our backend to determine if our password
# is in the list


def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # we receive the hashes list (the tails of the matching passwords, without the first five characters)
    # and hash_to_check, that is our password tail. So we convert in a list of tuples splitting by ':' and getting
    # the string to compare, and the number of times that has been leaked (the format we're receiving from api is
    # 003D68EB55068C33ACE09247EE4C639306B:3)

    # Also, we use splitlines() because what we receive is a string with many lines, and we want a list to iterate
    hashes = (line.split(':') for line in hashes.text.splitlines())

    # We iterate the list of tuples getting 'h' that is the string, and count that is the number of times
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # We need to hash the password with sha1 (this returns us a sha1 object, so we use hexdigest to get the string)
    # We convert into upperCase because is required by pwned api
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(f'"{password}" was found {count} times... you should probably change your password')
        else:
            print(f'"{password}" was NOT found. Carry on!')
    return 'done!'


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


