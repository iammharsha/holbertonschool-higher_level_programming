#!/usr/bin/python3
"""Write an object to text file"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to text file

    Args:
        my_object (object): JSON object to store in file
        filename (string): Name of the file to store JSON object
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
