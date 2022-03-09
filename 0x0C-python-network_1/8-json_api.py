#!/usr/bin/python3
"""
This module sends a letter as a post request to url
"""


if __name__ == '__main__':
    from requests import get, post
    from sys import argv
    if len(argv) < 2:
        q = ""
    else:
        q = argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    request = post(url, data={'q': q})
    try:
        postreply = request.json()
        id = postreply.get('id')
        name = postreply.get('name')
        if len(postreply) == 0:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except Exception:
        print("Not a valid JSON")
