#!/usr/bin/python3
"""Module to get status"""
import urllib.request


if __name__ == "__main__":
    """Module to call api https://intranet.hbtn.io/status"""
    url = 'https://intranet.hbtn.io/status'
    headers = {
       'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    }

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        content = response.read()
        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", content.decode('utf-8'))
