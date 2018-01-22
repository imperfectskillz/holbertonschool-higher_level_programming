#!/usr/bin/python3
"""
Module containing add item to json function
MUST IMPORT SYS TO USE ARGV
MUST IMPORT JSON TO USE JSON
USE TRY TO LOAD THE FILE
USE EXCEPT IF FILE DOESN'T EXIST
"""
from sys import argv
import json

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    temp = load_from_json_file("add_item.json")
except:
    temp = []

temp.extend(argv[1:])
save_to_json_file(temp, "add_item.json")
