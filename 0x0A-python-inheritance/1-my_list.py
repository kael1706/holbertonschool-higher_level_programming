#!/usr/bin/python3
"""
this is the module 1-my_list.
this module have the following classes:
MyList:
    print_sorted.
"""


class MyList(list):
    """class My_list extended of list."""

    def print_sorted(self):
        """print sort list."""
        print(sorted(self))
