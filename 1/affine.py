"""File: affine.py"""

import affine_common_data as acd
from key_error import key_error_str

alp, alp_ = acd.set_val()


def affine_enc(inp_str: str = "", k1: int = 0, k2: int = 0) -> str:
    """This function makes encryption of the affine cipher"""
    key_error_str(inp_str)

    enc_st = ""
    for i in range(len(inp_str)):
        enc_st += alp_[(k1 * alp[inp_str[i]] + k2) % 26]
    return enc_st


def affine_dec(inp_str: str = "", k1: int = 0, k2: int = 0) -> str:
    """This function makes decryption of the affine cipher"""
    key_error_str(inp_str)

    dec_st = ""
    for i in range(len(inp_str)):
        dec_st += alp_[(acd.find_x(k1) * (alp[inp_str[i]] - k2)) % 26]
    return dec_st
