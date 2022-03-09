#!/usr/bin/python3
"""
This module displays the response of a POST request
"""


if __name__ == '__main__':
    from urllib import request, parse
    import sys

    email = {'email': sys.argv[2]}
    data = parse.urlencode(email).encode('UTF-8')
    req = request.Request(sys.argv[1], email)

    with request.urlopen(req) as reply:
        html = reply.read()
        print(html.decode('UTF-8'))
