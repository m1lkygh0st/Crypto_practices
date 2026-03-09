"""File: key_error.py"""


def key_error_str(inp_str: str = ""):
    """This function outputs key error message for string"""
    for char in inp_str:
        if char.isdecimal():
            raise KeyError("Numbers not allowed in string")
        if not char.isalpha():
            raise KeyError("Unknown symbol not allowed in string")
