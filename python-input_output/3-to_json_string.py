#!/usr/bin/python3
"""Function that returns JSON representation of object (string)"""

import json


def to_json_string(my_obj):
    """
    Function that returns JSON representation of object (string)

    Args:
        my_obj (object): JSON object

    Returns:
        string: JSON representation of an object
    """
    return json.dumps(my_obj)
