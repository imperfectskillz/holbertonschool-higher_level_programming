#!/usr/bin/python3
"""
json api
"""
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1] is not None:
        q = argv[1]
    else:
        q = ""

    values = {'q': q}
    r = requests.post('http://0.0.0.0:5000/search_user', values)
    json = r.json()

    try:
        if json['id'] and json['name']:
            print("[{}] {}".format(json['id'], json['name']))
        else:
            print("Not a valid JSON")
    except:
        print("No result")
