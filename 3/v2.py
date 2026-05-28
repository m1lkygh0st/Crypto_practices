"""v2 module"""

from utils import is_english_letter, char_to_num, num_to_char


def v2_enc(text, key):
    """This function is used to manage the v2 encryption command"""
    res = ""
    key = "".join(ch.lower() for ch in key if is_english_letter(ch))

    if len(key) == 0:
        return text

    gamma = list(key)
    gamma_index = 0

    for ch in text:
        if is_english_letter(ch):
            x = char_to_num(ch)
            g = char_to_num(gamma[gamma_index])
            y = (x + g) % 26
            res += num_to_char(y, ch.isupper())
            gamma.append(ch.lower())
            gamma_index += 1
        else:
            res += ch

    return res


def v2_dec(text, key):
    """This function is used to manage the v2 decryption command"""
    res = ""
    key = "".join(ch.lower() for ch in key if is_english_letter(ch))

    if len(key) == 0:
        return text

    gamma = list(key)
    gamma_index = 0

    for ch in text:
        if is_english_letter(ch):
            y = char_to_num(ch)
            g = char_to_num(gamma[gamma_index])
            x = (y - g) % 26
            dec_char = num_to_char(x, ch.isupper())
            res += dec_char
            gamma.append(dec_char.lower())
            gamma_index += 1
        else:
            res += ch

    return res
