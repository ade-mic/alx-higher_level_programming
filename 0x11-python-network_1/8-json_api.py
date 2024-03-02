#!/usr/bin/python3
"""
Python script that takes in a letter and sends a
POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
import requests
from sys import argv


def main():
    """
    main fuction to not allow the code be executed
    when imported
    """
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""
    # Send a POST request
    base_url = "http://0.0.0.0:5000/search_user"
    response = requests.post(base_url, {'q': q})

    # Check if the response is valid JSON
    try:
        data = response.json()
        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    main()
