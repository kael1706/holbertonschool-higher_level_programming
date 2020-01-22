#!/usr/bin/python3
def to_json_string(my_obj):
    """
    return the JSON representation of an object (string)
    Object --> JSON
    """
    import json
    return json.dumps(my_obj)
