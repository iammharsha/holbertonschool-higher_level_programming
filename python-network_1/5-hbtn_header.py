#!/usr/bin/python3
"""Module to send request and print X-Request-Id"""
import sys
import requests


if __name__ == "__main__":
    """Module to send request and print X-Request-Id"""
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
