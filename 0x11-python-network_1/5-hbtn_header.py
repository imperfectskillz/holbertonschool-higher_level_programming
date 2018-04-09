#!/usr/bin/python3
"""
use request package display variable x-request
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers['X-Request_Id'])
