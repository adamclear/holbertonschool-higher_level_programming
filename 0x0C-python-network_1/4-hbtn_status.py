#!/usr/bin/python3
"""
This module fetches the status of the given url
"""


if __name__ == '__main__':
    from requests import get
    request = get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(request.text)))
    print("\t- content: {}".format(request.text))
