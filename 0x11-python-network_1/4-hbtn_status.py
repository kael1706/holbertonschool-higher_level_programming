#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""


import requests


if __name__ == '__main__':
    rps = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(rps.text)))
    print("\t- content: {}".format(rps.text))
