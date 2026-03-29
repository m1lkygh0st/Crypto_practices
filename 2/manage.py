"""File for managing the encryption and decryption module"""

from decode_hill import hill_known_plaintext_attack
from decode_hill_recur import recur_hill_known_plaintext_attack
from decode_utils import input_text
from hill import hill_encrypt, hill_decrypt
from hill_recur import recur_hill_encrypt, recur_hill_decrypt
from utils import input_matrix


def hill_manage():
    """This function is used to manage the hill command"""
    cmd = input("Choose a command:\n| encode - 1 | decode - 2 |\n")
    st = input("input string: ")
    n = int(input("Размер блока: "))
    key = input_matrix("K", n)
    if cmd == "1":
        try:
            print(hill_encrypt(st, key))
        except KeyError as e:
            print(f"KeyError: {e}")
    elif cmd == "2":
        try:
            print(hill_decrypt(st, key))
        except KeyError as e:
            print(f"KeyError: {e}")
    else:
        print("Unknown command")


def hill_recur_manage():
    """This function is used to manage the hill_recur command"""
    cmd = input("Choose a command:\n| encode - 1 | decode - 2 |\n")
    st = input("input string: ")
    n = int(input("Размер блока: "))
    key1 = input_matrix("K", n)
    key2 = input_matrix("K", n)
    if cmd == "1":
        try:
            print(recur_hill_encrypt(st, key1, key2))
        except KeyError as e:
            print(f"KeyError: {e}")
    elif cmd == "2":
        try:
            print(recur_hill_decrypt(st, key1, key2))
        except KeyError as e:
            print(f"KeyError: {e}")
    else:
        print("Unknown command")


def decode_hill_manage():
    """This function is used to manage the decoding of hill cipher"""
    n = int(input("Size of block n: "))
    if n < 1:
        raise ValueError("Input a positive integer")
    print(f"Need a minimum of {n * n} plaintext and ciphertext characters")
    plaintext = input_text("Known plaintext: ")
    ciphertext = input_text("Corresponding ciphertext: ")
    try:
        K = hill_known_plaintext_attack(plaintext, ciphertext, n)
        extra = input_text("\nCiphertext to decrypt with found keys: ")
        if extra:
            decrypted = hill_decrypt(extra, K)
            print(f"Decrypted: {decrypted}")
    except ValueError as e:
        print(f"\nError: {e}")


def decode_hill_recur_manage():
    """This function is used to manage the decoding of hill recur cipher"""
    n = int(input("Size of block n: "))
    if n < 1:
        raise ValueError("Input a positive integer")
    min_chars = max(2 * n, 4) * n
    print(f"Need a minimum of {min_chars} plaintext and ciphertext characters")
    plaintext = input_text("Known plaintext: ")
    ciphertext = input_text("Corresponding ciphertext: ")
    try:
        K1, K2 = recur_hill_known_plaintext_attack(plaintext, ciphertext, n)
        extra = input_text("\nCiphertext to decrypt with found keys: ")
        if extra:
            decrypted = recur_hill_decrypt(extra, K1, K2)
            print(f"Decrypted: {decrypted}")
    except ValueError as e:
        print(f"\nError: {e}")
