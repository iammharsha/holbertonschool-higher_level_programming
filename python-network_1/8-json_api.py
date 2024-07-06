#!/usr/bin/python3
"""Module for Search API"""
import sys
import requests


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    data = {'q': q}
    r = requests.post(url, data)
    try:
        body = r.json()
        if body:
            print("[{}] {}".format(body.get('id'), body.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
