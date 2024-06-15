#!/usr/bin/python3
"""Create object from JSON file"""

import json


def load_from_json_file(filename):
    """
    Create object from JSON file

    Args:
        filename (string): Name of file with JSON object

    Returns:
        object: JSON object read from file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
