#!/bin/bash
# POST request with variables
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
