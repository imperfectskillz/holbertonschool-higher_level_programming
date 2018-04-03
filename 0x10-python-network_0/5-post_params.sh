#!/bin/bash
# POST request with variables
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be there for PLD"
