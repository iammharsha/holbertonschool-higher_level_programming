#!/usr/bin/python3
"""Module to get GitHub id using GitHub API"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]

    r = requests.get(url, auth=(username, password))
    if r.status_code == 200:
        user_info = r.json()
        print(user_info.get('id'))
    else:
        print("None")
