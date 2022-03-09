#!/usr/bin/python3
"""
This module sends a POST request to an email and prints response
"""


if __name__ == '__main__':
    from requests import post
    from sys import argv
    email = {'email': argv[2]}
    request = post(argv[1], email)
    print(request.text)
