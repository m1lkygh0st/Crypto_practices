"""File affine_common_data.py"""

import string


def set_val():
    """This function sets values to variables"""
    alp = dict(zip(string.ascii_uppercase, range(26)))
    alp_ = dict(zip(range(26), string.ascii_uppercase))
    alp2 = dict(zip(string.ascii_lowercase, range(26)))
    alp2_ = dict(zip(range(26), string.ascii_lowercase))
    return alp, alp_, alp2, alp2_


def find_x(k1: int = 0) -> int | None:
    """This function finds the unknown number"""
    for i in range(1, 27):
        if (k1 * i) % 26 == 1:
            return i
    return None
