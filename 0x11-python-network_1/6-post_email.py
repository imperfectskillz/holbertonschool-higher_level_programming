#!/usr/bin/python3
"""
POST using requests
"""
import requests
from sys import argv


if __name__ == "__main__":
    payload = {'e-mail': argv[2]}
    r = requests.post(argv[1], data=payload)
    print(r.text)
