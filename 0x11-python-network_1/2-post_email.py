#!/usr/bin/python3
"""
takes in a URL and an email,
sends a POST request to the passed
URL with theemail as a parameter,
and displays the body of the response
"""


from urllib import request, parse
from sys import argv


if __name__ == '__main__':
    d = parse.urlencode(
                           {'email': argv[2]}
                       ).encode('ascii')
    with request.urlopen(argv[1], d) as rps:
        html5 = rps.read()
        print(html5.decode('utf-8'))
