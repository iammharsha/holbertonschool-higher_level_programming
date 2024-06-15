#!/usr/bin/python3
"""Script to adds all arguments to Python list and then save them to file"""


import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

args = sys.argv[1:]

try:
    list = load_from_json_file(filename)
except FileNotFoundError:
    list = []

list.extend(args)

save_to_json_file(list, filename)
