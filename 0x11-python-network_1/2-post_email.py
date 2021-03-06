#!/usr/bin/python3
"""
POST request
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    values = {'email': argv[2]}
    url = argv[1]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf-8'))
