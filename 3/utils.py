"""Utils module"""


def is_english_letter(ch):
    """This function is used to manage the command"""
    return "a" <= ch <= "z" or "A" <= ch <= "Z"


def char_to_num(ch):
    """This function is used to manage the command"""
    return ord(ch.lower()) - ord("a")


def num_to_char(num, is_upper=False):
    """This function is used to manage the command"""
    ch = chr(num + ord("a"))
    return ch.upper() if is_upper else ch
