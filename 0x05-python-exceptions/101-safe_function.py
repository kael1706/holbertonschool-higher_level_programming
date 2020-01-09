#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as error_description:
        print("Exception: {}".format(error_description), file=sys.stderr)
