"""File: affine_recur.py"""

import affine_common_data as acd
import key_error


def affine_recurs_enc(inp_str: str = "", k1=None, k2=None) -> str:
    """Encryption with affine recurrent cipher"""

    key_error.key_error_str(inp_str)
    for i in range(len(inp_str) - len(k1)):
        k1.append((k1[-1] * k1[-2]) % 26)
        k2.append((k2[-1] + k2[-2]) % 26)

    return "".join(
        chr((k1[i] * (ord(ch) - 65) + k2[i]) % 26 + 65)
        if "A" <= ch <= "Z"
        else chr((k1[i] * (ord(ch) - 97) + k2[i]) % 26 + 97)
        if "a" <= ch <= "z"
        else ch
        for i, ch in enumerate(inp_str)
    )


def affine_recurs_dec(inp_str: str = "", k1=None, k2=None) -> str:
    """Decryption with affine recurrent cipher"""

    key_error.key_error_str(inp_str)
    for i in range(len(inp_str) - len(k1)):
        k1.append((k1[-1] * k1[-2]) % 26)
        k2.append((k2[-1] + k2[-2]) % 26)

    return "".join(
        chr((acd.find_x(k1[i]) * (ord(ch) - 65 - k2[i])) % 26 + 65)
        if "A" <= ch <= "Z"
        else chr((acd.find_x(k1[i]) * (ord(ch) - 97 - k2[i])) % 26 + 97)
        if "a" <= ch <= "z"
        else ch
        for i, ch in enumerate(inp_str)
    )
