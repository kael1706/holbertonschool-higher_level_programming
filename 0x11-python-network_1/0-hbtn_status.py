#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""


from urllib import request


if __name__ == '__main__':
    with request.urlopen("https://intranet.hbtn.io/status") as rps:
        r = rps.read()
        print("Body response:")
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
        print("\t- utf8 content: {}".format(r.decode("utf-8")))
