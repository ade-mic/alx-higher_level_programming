#!/usr/bin/python3
"""
A Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found
in the header of the response.
"""
import requests
from sys import argv


def main():
    """
    main fuction to not allow the code be executed
    when imported
    """
    req = requests.get('{}'.format(argv[1]))
    x_request_id = req.headers.get("X-Request-Id")
    print(x_request_id)


if __name__ == "__main__":
    main()
