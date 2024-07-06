#!/usr/bin/python3
"""Script that takes in URL and display X-Request-Id header value"""
import sys
import urllib.request


if __name__ == "__main__":
    """
    Script that takes URL and display X-Request-Id header value

    Args:
        args: Command Line argument containing URL to be called
    """
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        x_request_id = response.headers.get('X-Request-Id'):
        print(x_request_id)
