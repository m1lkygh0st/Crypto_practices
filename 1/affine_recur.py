"""File: affine_recur.py"""

import string

letters = list(string.ascii_uppercase)
num = [int(i) for i in range(26)]
alp = dict(zip(letters, num))
alp_ = dict(zip(num, letters))


def find_x(k1: int = 0) -> int | None:
    """This function finds the unknown number"""
    for i in range(1, 27):
        if (k1 * i) % 26 == 1:
            return i
    return None


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
        dec_st += alp_[(find_x(k1[i]) * (alp[st[i]] - k2[i])) % 26]
    return dec_st
