#!/usr/bin/python3
"""Module to get status usin requests"""
import requests


if __name__ == "__main__":
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    r = requests.get('https://intranet.hbtn.io/status', headers=headers)
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
