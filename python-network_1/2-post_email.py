#!/usr/bin/python3
"""Module to send url request with body using POST"""
import sys
import urllib.request


if __name__ == "__main__":
    """
    Send Post request with url and email and print response body

    Argv:
        string: URL of request
        string: E-Mail ID
    """
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)
