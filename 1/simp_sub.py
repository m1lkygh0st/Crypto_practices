"""File: simp_sub.py"""

import string

from key_error import key_error_str, key_error_alp


def simp_sub_enc(inp_str: str = "", inp_alp: str = "") -> str:
    """This function makes encryption of the simple substitution cipher"""
    key_error_str(inp_str)
    key_error_alp(inp_alp)

    alp = dict(zip(string.ascii_uppercase, range(26)))
    alp_ = dict(zip(range(26), inp_alp))
    new_str = ""
    for i in inp_str:
        new_str += alp_[alp[i]]
    return new_str


def simp_sub_dec(inp_str: str = "", inp_alp: str = "") -> str:
    """This function makes decryption of the simple substitution cipher"""
    key_error_str(inp_str)
    key_error_alp(inp_alp)

    alp = dict(zip(inp_alp, range(26)))
    alp_ = dict(zip(range(26), string.ascii_uppercase))
    new_str = ""
    for i in inp_str:
        new_str += alp_[alp[i]]
    return new_str
