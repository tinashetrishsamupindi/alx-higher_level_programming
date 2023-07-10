#!/usr/bin/python3
"""
File: 2-is_same_clas.py
Desc: This module has one function; is_same_class
Author: Onyejekwe  Philip (Donphili)
Date Created: 09 jun 2023
"""


def is_same_class(obj, a_class):
    """
    Returns true if object is exactly an instance of
    specified class, otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
