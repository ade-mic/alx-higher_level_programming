#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


def main():
    """ Main fuction to not allow the code be executed
    when imported """
    import requests
    req = requests.get('https://alx-intranet.hbtn.io/status')
    hbtn_page = req.text
    print('Body response:')
    print('\t- type: {}'.format(type(hbtn_page)))
    print('\t- content: {}'.format(hbtn_page))


if __name__ == "__main__":
    main()
