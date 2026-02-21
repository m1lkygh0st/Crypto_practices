"""File affine_common_data.py"""

import string


def set_val():
    """This function sets values to variables"""
    letters = list(string.ascii_uppercase)
    num = [int(i) for i in range(26)]
    alp = dict(zip(letters, num))
    alp_ = dict(zip(num, letters))
    return letters, num, alp, alp_


def find_x(k1: int = 0) -> int | None:
    """This function finds the unknown number"""
    for i in range(1, 27):
        if (k1 * i) % 26 == 1:
            return i
    return None
