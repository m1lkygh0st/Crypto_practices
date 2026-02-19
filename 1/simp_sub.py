"""File: simp_sub.py"""

import string


def simp_sub_enc(inp_str, letters2):
    """This function makes encryption of the simple substitution cipher"""
    letters = list(string.ascii_uppercase)
    num = [int(i) for i in range(26)]
    alp = dict(zip(letters, num))
    alp2_ = dict(zip(num, letters2))
    digits = []
    for i in inp_str:
        digits.append(alp[i])
    new_str = ""
    for i in digits:
        new_str += alp2_[i]
    return new_str


def simp_sub_dec(inp_str, letters2):
    """This function makes decryption of the simple substitution cipher"""
    letters = list(string.ascii_uppercase)
    num = [int(i) for i in range(26)]
    alp_ = dict(zip(num, letters))
    alp2 = dict(zip(letters2, num))
    digits = []
    for i in inp_str:
        digits.append(alp2[i])
    new_str = ""
    for i in digits:
        new_str += alp_[i]
    return new_str
