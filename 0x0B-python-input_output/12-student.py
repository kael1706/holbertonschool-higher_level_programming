#!/usr/bin/python3
class Student():
    """class Student."""

    def __init__(self, first_name, last_name, age):
        """initialize class attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance."""
        if attrs is None:
            if hasattr(self, '__dict__'):
                return self.__dict__
            if hasattr(self, '__slots__'):
                return self.__slots__

        if attrs is not None and isinstance(attrs, list) == False:
            if hasattr(self, '__dict__'):
                return self.__dict__
            if hasattr(self, '__slots__'):
                return self.__slots__

        if attrs is not None:
            if all(isinstance(item, str) for item in attrs):
                a = {}
                for pos, v in self.__dict__.items():
                    if pos in attrs:
                        a[pos] = v
                return a
