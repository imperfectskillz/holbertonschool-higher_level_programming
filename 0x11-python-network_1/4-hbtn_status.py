#!/usr/bin/python3
"""
fetch using package requests
"""
import requests


if __name__ == "__main__":
    r = requests.get(argv[1])
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text)))
