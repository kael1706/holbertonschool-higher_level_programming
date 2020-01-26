#!/usr/bin/python3
"""
this is the module rectangule.
this module has the following classes:
Rectangle.
"""

from models.base import Base


def int_check(n, v):
    """check if is a valid integer."""
    w = ['width', 'height', 'x', 'y']
    if type(v) != int:
        raise TypeError("{} must be an integer".format(n))
    if (n == w[0] or n == [1]) and v <= 0:
        raise ValueError("{} must be > 0".format(n))
    if (n == w[2] or n == w[3]) and v < 0:
        raise ValueError("{} must be >= 0".format(n))


class Rectangle(Base):
    """Rectangle class extends from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialize the attributtes."""
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """return the area of the instance."""
        return self.__width * self.__height

    def display(self):
        """draw the object"""
        if (self.area() == 0):
            print('')
            return
        for axis_y in range(0, self.__y):
            print('')
        for h in range(0, self.__height):
            for x in range(0, self.__x):
                print(' ', end='')
            for w in range(0, self.__width):
                print('#', end='')
            print('')

    def update(self, *args, **kwargs):
        """
        Overwrite multiple attribute values.
        indeterminate arguments by position
        and name are used.
        """
        if args:
            l = ['id', 'width', 'height', 'x', 'y']
            for idx, v in enumerate(args):
                setattr(self, l[idx], v)
            return
        for k in kwargs:
            if hasattr(self, k):
                setattr(self, k, kwargs[k])

    def __str__(self):
        """
        Instance method that returns an “informal”
        and nicely printable string representation
        of an instance
        """
        return ('[Rectangle] ({}) {}/{} - {}/{}'.format(self.id,
                self.__x, self.__y, self.__width, self.__height))

    def to_dictionary(self):
        """return dict of the instance"""
        d = self.__dict__
        newd = {}
        new_k = ''
        if d:
            for k in d:
                new_k = k
                if k.startswith('_'):
                    new_k = k[12:]
                newd[new_k] = d[k]
            return newd

    @property
    def width(self):
        """get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """set width."""
        int_check('width', value)
        self.__width = value

    @property
    def height(self):
        """get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """set height."""
        int_check('height', value)
        self.__height = value

    @property
    def x(self):
        """get x."""
        return self.__x

    @x.setter
    def x(self, value):
        """set x."""
        int_check('x', value)
        self.__x = value

    @property
    def y(self):
        """get y."""
        return self.__y

    @y.setter
    def y(self, value):
        """set y."""
        int_check('y', value)
        self.__y = value
