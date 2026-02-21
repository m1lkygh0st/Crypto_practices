"""File: affine_recur.py"""

import affine_common_data as acd

letters, num, alp, alp_ = acd.set_val()


def affine_recurs_enc(st: str = "", k1=None, k2=None) -> str:
    """This function makes decryption of the affine recurrent cipher"""
    enc_st = ""
    for i in range(len(st)):
        enc_st += alp_[(k1[i] * alp[st[i]] + k2[i]) % 26]
    return enc_st


def affine_recurs_dec(st: str = "", k1=None, k2=None) -> str:
    """this function makes decryption of the affine recurrent cipher"""
    dec_st = ""
    for i in range(len(st)):
        dec_st += alp_[(acd.find_x(k1[i]) * (alp[st[i]] - k2[i])) % 26]
    return dec_st
