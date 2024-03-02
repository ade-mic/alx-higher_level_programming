#!/usr/bin/python3
"""
Python script that takes your GitHub credentials 
(username and password) and uses the GitHub API 
to display your id
"""
import requests
from sys import argv


def main():
    """
    main fuction to not allow the code be executed
    when imported
    """

    # password and user
    username = argv[1]
    password = argv[2]
    # Send a POST request
    base_url = "https://api.github.com/user"
    response = requests.get(base_url, auth=(username, password))

    # Check if the response is valid JSON
    data = response.json()
    print("{}".format(data.get('id')))


if __name__ == "__main__":
    main()
