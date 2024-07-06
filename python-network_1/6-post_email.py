#!/usr/bin/python3
"""Module to send POST request"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    r = requests.post(url, data)
    print(r.text)
