#!/usr/bin/python3
"""
use star wars API send string
"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get("http://swapi.co/api/people/?search={}".format
                            (argv[1]))
    json = response.json()
    print("Number of results: {}".format(json['count']))

    for x in json['results']:
        print(x['name'])
