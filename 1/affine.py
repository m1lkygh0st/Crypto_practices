"""File: affine.py"""

import string
import affine_common_data as acd
import key_error


def affine_enc(inp_str: str = "", k1: int = 0, k2: int = 0) -> str:
    """Encryption with affine cipher"""

    key_error.key_error_str(inp_str)
    return "".join(
        string.ascii_uppercase[(k1 * (ord(i) - ord("A")) + k2) % 26]
        if i.isupper()
        else string.ascii_lowercase[(k1 * (ord(i) - ord("a")) + k2) % 26]
        if i.isalpha()
        else i
        for i in inp_str
    )


def affine_dec(inp_str: str, k1: int, k2: int) -> str:
    """Decryption with affine cipher"""

    key_error.key_error_str(inp_str)
    x = acd.find_x(k1)

    def dec_char(char: str, k1_inv: int, k2_inv: int, num: int) -> str:
        """Decryption of the single character with affine cipher"""
        idx = ord(char) - num
        return chr(((k1_inv * (idx - k2_inv)) % 26) + num)

    return "".join(
        dec_char(i, x, k2, ord("A"))
        if i.isupper()
        else dec_char(i, x, k2, ord("a"))
        if i.islower()
        else i
        for i in inp_str
    )
