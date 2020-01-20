#!/usr/bin/python3
"""
this is the module 7-base_geometry.
this module have the following classes:
BaseGeomtry:
    area(self): print a Exption msg
    integer_validator: check if is a valid int
"""


class BaseGeometry():
    """Class BaseGeometry"""

    def area(self):
        """ print a Exception msg"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if is a valid int"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
