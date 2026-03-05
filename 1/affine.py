"""File: affine.py"""

import string

import affine_common_data as acd
from key_error import key_error_str

alp, alp_, alp2, alp2_ = acd.set_val()


def affine_enc(inp_str: str = "", k1: int = 0, k2: int = 0) -> str:
    """This function makes encryption of the affine cipher"""
    key_error_str(inp_str)

    enc_st = ""

    for i in inp_str:
        if i in string.ascii_uppercase:
            enc_st += alp_[(k1 * alp[i] + k2) % 26]
        else:
            enc_st += alp2_[(k1 * alp2[i] + k2) % 26]
    return enc_st


def affine_dec(inp_str: str = "", k1: int = 0, k2: int = 0) -> str:
    """This function makes decryption of the affine cipher"""
    key_error_str(inp_str)

    dec_st = ""
    for i in inp_str:
        if i in string.ascii_uppercase:
            dec_st += alp_[(acd.find_x(k1) * (alp[i] - k2)) % 26]
        else:
            dec_st += alp2_[(acd.find_x(k1) * (alp2[i] - k2)) % 26]
    return dec_st
