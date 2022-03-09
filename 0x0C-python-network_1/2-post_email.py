#!/usr/bin/python3
"""
This module displays the response of a POST request
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    from sys import argv

    email = {'email': argv[2]}
    data = urlencode(email).encode('utf-8')
    request = Request(argv[1], data)

    with urlopen(request) as reply:
        print(reply.read().decode('utf-8'))
