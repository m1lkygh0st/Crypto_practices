"""v1 module"""

from utils import is_english_letter, char_to_num, num_to_char


def v1_enc(text, key):
    """This function is used to manage the v1 encryption command"""
    res = ""
    key = "".join(ch.lower() for ch in key if is_english_letter(ch))

    if len(key) == 0:
        return text

    key_index = 0
    key_len = len(key)

    for ch in text:
        if is_english_letter(ch):
            x = char_to_num(ch)
            k = char_to_num(key[key_index % key_len])
            y = (x + k) % 26
            res += num_to_char(y, ch.isupper())
            key_index += 1
        else:
            res += ch

    return res


def v1_dec(text, key):
    """This function is used to manage the v1 decryption command"""
    res = ""
    key = "".join(ch.lower() for ch in key if is_english_letter(ch))

    if len(key) == 0:
        return text

    key_index = 0
    key_len = len(key)

    for ch in text:
        if is_english_letter(ch):
            y = char_to_num(ch)
            k = char_to_num(key[key_index % key_len])
            x = (y - k) % 26
            res += num_to_char(x, ch.isupper())
            key_index += 1
        else:
            res += ch

    return res
