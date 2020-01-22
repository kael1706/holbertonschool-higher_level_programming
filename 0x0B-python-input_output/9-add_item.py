#!/usr/bin/python3
"""
script that adds all arguments to a Python list,
and then save them to a file.

load_from_json_file: creates an Object from a “JSON file”
save_to_json_file: write an Object to a text file,
using a JSON representation.
"""
import sys
import os
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
append_write = __import__('4-append_write').append_write


args = sys.argv[1:]
l = []

if os.path.exists('add_item.json'):
        l = load_from_json_file('add_item.json')
        save_to_json_file(l + args, 'add_item.json')
else:
    append_write('add_item.json', '[]')
    l = load_from_json_file('add_item.json')
    save_to_json_file(l + args, 'add_item.json')
