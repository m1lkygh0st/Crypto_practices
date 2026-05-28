"""Main module"""

import itertools
from crypto_utils import ALPHABET
from v1 import v1_enc, v1_dec
from v2 import v2_enc, v2_dec
from v3 import v3_enc, v3_dec
from cr_1 import v_11, v_12
from cr_2 import v_22
from cr_3 import v_33


def v1_manage(text, key, cmd):
    """This function is used to manage the v1 command"""

    if cmd == "1":
        result = v1_enc(text, key)
    elif cmd == "2":
        result = v1_dec(text, key)
    else:
        result = "Error: Incorrect mode selected"
    print(result)


def v2_manage(text, key, cmd):
    """This function is used to manage the v2 command"""
    if cmd == "1":
        result = v2_enc(text, key)
    elif cmd == "2":
        result = v2_dec(text, key)
    else:
        result = "Error: Incorrect mode selected"
    print(result)


def v3_manage(text, key, cmd):
    """This function is used to manage the v3 command"""
    if cmd == "1":
        result = v3_enc(text, key)
    elif cmd == "2":
        result = v3_dec(text, key)
    else:
        result = "Error: Incorrect mode selected"
    print(result)


def v11_manage():
    """This function is used to manage the v22 command"""
    print("Vigenere's Universal Cryptanalysis")

    raw_ciphertext = input("Input the encrypted text: ").strip()

    choice = input("""
    Select mode:
    1 - Analysis (Kaziski Test + Smart Search Top 10 Probable Keyword Search)
    2 - Full brute force (displaying ALL possible combinations on the screen)
    """)

    try:
        key_length = int(input("Input the expected key length: "))
    except ValueError:
        print("Error: Key length must be a number")

    all_possible_keys = itertools.product(ALPHABET, repeat=key_length)

    if choice == "1":
        v_11(raw_ciphertext, key_length, all_possible_keys)

    elif choice == "2":
        v_12(raw_ciphertext, key_length, all_possible_keys)
    else:
        print(ValueError("Mode should be 1 or 2"))


def v22_manage():
    print("Cryptanalysis of Vigenère's self-key")

    ciphertext = input("Input the encrypted text: ").strip()
    if not ciphertext:
        print(ValueError("Text is empty"))

    print("\n[*] Going through all 26 variants of the initial symbol...")
    v_22(ciphertext)


def v33_manage():
    print("Cryptanalysis of a self-key using CIFRTEXT")

    ciphertext = input("Input the encrypted text: ").strip()
    if not ciphertext:
        print(ValueError("Text is empty"))

    print("\n[*] Going through all 26 variants of the initial symbol...")
    v_33(ciphertext)
