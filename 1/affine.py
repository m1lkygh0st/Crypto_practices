"""File: affine.py"""

import affine_common_data as acd

letters, num, alp, alp_ = acd.set_val()


def affine_enc(st: str = "", k1: int = 0, k2: int = 0) -> str:
    """This function makes encryption of the affine cipher"""
    enc_st = ""
    for i in range(len(st)):
        enc_st += alp_[(k1 * alp[st[i]] + k2) % 26]
    return enc_st


def affine_dec(st: str = "", k1: int = 0, k2: int = 0) -> str:
    """This function makes decryption of the affine cipher"""
    dec_st = ""
    for i in range(len(st)):
        dec_st += alp_[(acd.find_x(k1) * (alp[st[i]] - k2)) % 26]
    return dec_st
