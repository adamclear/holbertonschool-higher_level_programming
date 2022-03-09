#!/usr/bin/python3
"""
This module displays the response of a POST request
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    import sys

    email = {'email': sys.argv[2]}
    data = urlencode(email).encode('UTF-8')
    req = Request(sys.argv[1], email)

    with urlopen(req) as reply:
        print(reply.read().decode('UTF-8'))
