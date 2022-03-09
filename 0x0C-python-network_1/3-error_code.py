#!/usr/bin/python3
"""
This module takes in a URL and displays the response to a request
"""


if __name__ == '__main__':
    from urllib.request import Request, urlopen
    from urllib.error import HTTPError
    from sys import argv

    request = Request(argv[1])
    try:
        with urlopen(request) as reply:
            reply = reply.read()
            print(reply.decode('utf-8'))
    except HTTPError as error:
        print("Error code: {}".format(error.code))
