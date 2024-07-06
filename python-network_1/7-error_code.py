#!/usr/bin/python3
"""Module to handle HTTP error using requests"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    r = requests.get(url)
    status_code = r.status_code
    if status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
