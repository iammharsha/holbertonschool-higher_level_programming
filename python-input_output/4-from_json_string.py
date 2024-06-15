#!/usr/bin/python3
"""Function that returns object represented by a JSON string"""

import json


def from_json_string(my_str):
    """
    Function that returns object represented by a JSON string

    Args:
        my_str (string): JSON string

    Returns:
        object: JSON object
    """
    return json.loads(my_str)
