#!/usr/bin/python3
"""
A  Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import requests
from sys import argv


def main():
    """
    main fuction to not allow the code be executed
    when imported
    """
    req = requests.get(argv[1])
    if req.status_code >= 400:
        print("Error code: {}".format(req.status_code))
    else:
        print(req.text)


if __name__ == "__main__":
    main()
