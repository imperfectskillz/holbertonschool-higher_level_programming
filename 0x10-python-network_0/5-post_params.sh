#!/bin/bash
# POST request with variables
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be there for PLD" "$1"
