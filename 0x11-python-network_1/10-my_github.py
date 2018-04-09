#!/usr/bin/python3
"""
use star wars API send string
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    json = r.json()
    if json:
        print(json['id'])
    else:
        print("None")
