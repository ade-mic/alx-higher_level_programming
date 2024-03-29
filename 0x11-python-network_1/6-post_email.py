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
    values = {}
    values['email'] = argv[2]
    req = requests.post(argv[1], values)
    body_res = req.text
    print(body_res)


if __name__ == "__main__":
    main()
