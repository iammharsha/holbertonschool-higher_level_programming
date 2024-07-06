#!/usr/bin/python3
"""Module to send request and display body or error status code"""
import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    """
    Module to send request and display body or error status code

    Argv:
        string: URL to send request
    """
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
