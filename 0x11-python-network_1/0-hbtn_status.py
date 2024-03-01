#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""


def main():
    """ Main fuction to not allow the code be executed
    when imported """
    import urllib.request
    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        hbtn_page = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(hbtn_page)))
        print('\t- content: {}'.format(hbtn_page))
        print('\t- utf8 content: {}'.format(hbtn_page.decode('utf-8')))


if __name__ == "__main__":
    main()
