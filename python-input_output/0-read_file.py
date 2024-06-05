#!/usr/bin/python3
"""This module contains function read_file"""


def read_file(filename=""):
    """
    Function to read and print file in UTF-8 format to stdout

    Args:
        filename (str): Name of the file to be read. Default is empty string.
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end='')
