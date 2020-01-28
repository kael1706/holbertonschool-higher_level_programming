#!/usr/bin/python3
"""
this is the module base.
this module has the followings classes:
base.
"""
import json
import os


class Base():
    """Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize attributes."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return JSON string representation of dictionary list."""
        e_msj = "list_dictionaries must be a list of dictionaries"
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError(e_msj)
        for item in list_dictionaries:
            if isinstance(item, dict) is False:
                raise TypeError(e_msj)
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save a obj as JSON string in json file."""
        l_o = []
        if not list_objs or list_objs is None:
            l_o = []
        else:
            for obj in list_objs:
                l_o.append(obj.to_dictionary())
        with open(cls.__name__ + '.json', 'w+', encoding='utf-8') as f:
            f.write(cls.to_json_string(l_o))
        f.close()

    @staticmethod
    def from_json_string(json_string):
        """Return dictionary list."""
        if not json_string or json_string is None:
            return []
        if type(json_string) != str:
            raise TypeError("json_string must be a string")
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return a instance with all attributes already set."""
        if cls.__name__ == 'Square':
            new_i = cls(1)
        else:
            new_i = cls(1, 1)
        new_i.update(**dictionary)
        return new_i

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        f_name = cls.__name__ + '.json'
        l_i = []
        if not os.path.exists(f_name):
            return []
        with open(f_name, 'r', encoding='utf-8') as j_f:
            l_d = cls.from_json_string(j_f.read())
        for d in l_d:
            l_i.append(cls.create(**d))
        return l_i
