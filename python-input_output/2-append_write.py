#!/usr/bin/python3
"""Append string to end of text file and return no of chars added"""


def append_write(filename="", text=""):
    """
    Append string to end of file in UTF-8 format and return no of char added

    Args:
        filename (str): Name of the file to be read. Default is empty string.
        text (str): String to be written to file. Default is empty string.

    Returns:
        int: Number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
