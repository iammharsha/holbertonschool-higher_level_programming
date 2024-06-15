#!/usr/bin/python3
"""Script to convert object into JSON-serializable dictionary representation"""


def class_to_json(obj):
    """
    Convert an object into a JSON-serializable dictionary representation.

    Args:
        obj: Instance of class

    Returns:
        dict: A dictionary containing JSON-serializable attributes of object.
    """
    attributes = obj.__dict__

    json_dict = {}

    for attr, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
