#!/usr/bin/python3
"""
A Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found
in the header of the response.
"""
import urllib.request
import os


def main():
    """
    main fuction to not allow the code be executed
    when imported
    """
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        x_request_id = response.getheader("X-Request-Id")
        print(x_request_id)


if __name__ == "__main__":
    main()
