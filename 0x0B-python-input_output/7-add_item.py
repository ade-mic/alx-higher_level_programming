#!/usr/bin/python3
"""
a script that adds all arguments
to a Python list, and then save them to a
file named add_item.json
"""

import sys
import os
# import save_to_json_file and load_from_json_file function
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
# filename
filename = 'add_item.json'
# variable to iterate through arguement
i = 1
args = []
for i in range(1, len(sys.argv)):
    args.append(sys.argv[i])

# check if file doesnt exist
if not os.path.exists(filename):
    save_to_json_file(args, filename)
else:
    load_args = load_from_json_file(filename)
    save_to_json_file(load_args + args, filename)
