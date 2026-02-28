"""File: key_error.py"""

import string


def key_error_str(inp_str: str = ""):
    """This function outputs key error message for string"""
    for char in inp_str:
        if char.isdecimal():
            raise KeyError("Numbers not allowed in string")
        if char in set(string.punctuation):
            raise KeyError("Marks not allowed in string")
        if not char.isalpha():
            raise KeyError("Unknown symbol not allowed in string")


def key_error_alp(inp_alp: str = ""):
    """This function outputs key error message for alphabet"""
    for char in inp_alp:
        if char.isdecimal():
            raise KeyError("Numbers not allowed in alphabet")
        if char in set(string.punctuation):
            raise KeyError("Marks not allowed in alphabet")
        if char == " ":
            raise KeyError("Space not allowed in alphabet")
        if not char.isalpha():
            raise KeyError("Unknown symbol not allowed in alphabet")
