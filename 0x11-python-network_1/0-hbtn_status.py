#!/usr/bin/python3
"""
A Python script that fetches https://alx-intranet.hbtn.io/status
"""
""" Main fuction to not allow the code be executed
when imported """
import urllib.request
req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    hbtn_page = response.read()
    print('- type: {}'.format(type(hbtn_page)))
    print('- content: {}'.format(hbtn_page))
    print('- utf8 content: {}'.format(hbtn_page.decode('utf-8')))
