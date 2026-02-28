"""File affine_common_data.py"""

import string


def set_val():
    """This function sets values to variables"""
    alp = dict(zip(string.ascii_uppercase, range(26)))
    alp_ = dict(zip(range(26), string.ascii_uppercase))
    return alp, alp_


def find_x(k1: int = 0) -> int | None:
    """This function finds the unknown number"""
    for i in range(1, 27):
        if (k1 * i) % 26 == 1:
            return i
    return None
