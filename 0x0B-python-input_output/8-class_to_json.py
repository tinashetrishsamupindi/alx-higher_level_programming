#!/usr/bin/python3
"""
Desc: This module contains one function; class_to_json(obj)
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object
    """
    return obj.__dict__
