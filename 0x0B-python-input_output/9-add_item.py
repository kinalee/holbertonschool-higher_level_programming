#!/usr/bin/python3
"""
9-add_item
"""
import sys
import json
import os.path

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if os.path.exists("add_item.json"):
    obj = load_from_json_file("add_item.json")
else:
    obj = []

obj = obj + sys.argv[1:]
save_to_json_file(obj, "add_item.json")
load_from_json_file("add_item.json")
