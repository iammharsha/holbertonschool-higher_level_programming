#!/usr/bin/python3
"""This module contains function write_file"""


def write_file(filename="", text=""):
    """
    Write string to text file in UTF-8 format and return no of char written

    Args:
        filename (str): Name of the file to be read. Default is empty string.
        text (str): String to be written to file. Default is empty string.
    """
    with open(filename, 'w', encoding="utf-8") as file:
        return file.write(text)
