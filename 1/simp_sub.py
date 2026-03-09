"""File: simp_sub.py"""

import string
import key_error


def simp_sub_enc(inp_str: str = "", inp_alp: str = "") -> str:
    """Encryption with simp_sub cipher"""

    key_error.key_error_str(inp_str)
    key_error.key_error_str(inp_alp)
    table = str.maketrans(string.ascii_uppercase + string.ascii_lowercase, inp_alp + inp_alp.lower())
    return inp_str.translate(table)


def simp_sub_dec(inp_str: str = "", inp_alp: str = "") -> str:
    """Decryption with simp_sub cipher"""

    key_error.key_error_str(inp_str)
    key_error.key_error_str(inp_alp)
    table = str.maketrans(inp_alp + inp_alp.lower(), string.ascii_uppercase + string.ascii_lowercase)
    return inp_str.translate(table)
