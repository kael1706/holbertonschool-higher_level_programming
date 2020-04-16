#!/usr/bin/python3
"""
Takes in a URL,
sends a request to the URL and
displays the body of the response.
"""


import requests
from sys import argv


if __name__ == '__main__':
    rps = requests.get(argv[1])
    e_code = rps.status_code
    if e_code >= 400:
        print("Error code: {}".format(str(e_code)))
    else:
        print(rps.text)
