#!/usr/bin/python3
"""
A  Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)
"""
import urllib
from sys import argv


def main():
    """
    main fuction to not allow the code be executed
    when imported
    """
    values = {}
    values['email'] = argv[2]
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as response:
        body_res = response.read().decode('utf-8')
        print(body_res)


if __name__ == "__main__":
    main()
