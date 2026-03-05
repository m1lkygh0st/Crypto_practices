"""File: affine_recur.py"""

import string
import affine_common_data as acd
from key_error import key_error_str

alp, alp_, alp2, alp2_ = acd.set_val()


def affine_recurs_enc(inp_str: str = "", k1=None, k2=None) -> str:
    """This function makes decryption of the affine recurrent cipher"""
    key_error_str(inp_str)

    enc_st = ""
    for i in range(len(inp_str)):
        if inp_str[i] in string.ascii_uppercase:
            enc_st += alp_[(k1[i] * alp[inp_str[i]] + k2[i]) % 26]
        else:
            enc_st += alp2_[(k1[i] * alp2[inp_str[i]] + k2[i]) % 26]
    return enc_st


def affine_recurs_dec(inp_str: str = "", k1=None, k2=None) -> str:
    """this function makes decryption of the affine recurrent cipher"""
    key_error_str(inp_str)

    dec_st = ""
    for i in range(len(inp_str)):
        if inp_str[i] in string.ascii_uppercase:
            dec_st += alp_[(acd.find_x(k1[i]) * (alp[inp_str[i]] - k2[i])) % 26]
        else:
            dec_st += alp2_[(acd.find_x(k1[i]) * (alp2[inp_str[i]] - k2[i])) % 26]
    return dec_st
