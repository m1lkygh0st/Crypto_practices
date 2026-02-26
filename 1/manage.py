"""File: manage.py"""

import simp_sub
import affine
import affine_recur
import decode_affine


def simp_sub_manage():
    """This function is used to manage the simp_sub command"""
    cmd = input("Choose a command:\n| encode - 1 | decode - 2 |\n")
    st, letters2 = input("input two strings with the space: ").split()
    if cmd == "1":
        print(simp_sub.simp_sub_enc(st, letters2))
    elif cmd == "2":
        print(simp_sub.simp_sub_dec(st, letters2))
    else:
        print("Unknown command")


def affine_manage():
    """This function is used to manage the affine command"""
    cmd = input("Choose a command:\n| encode - 1 | decode - 2 |\n")
    st = input("input string: ")
    a, b = map(int, input("input two digits with the space: ").split())
    if cmd == "1":
        print(affine.affine_enc(st, a, b))
    elif cmd == "2":
        print(affine.affine_dec(st, a, b))
    else:
        print("Unknown command")


def affine_recur_manage():
    """This function is used to manage the affine_recur command"""
    cmd = input("Choose a command:\n| encode - 1 | decode - 2 |\n")
    st = input("input string: ")
    a = list(map(int, input("input two digits with the space: ").split()))
    b = list(map(int, input("input two digits with the space: ").split()))

    while len(st) > len(a):
        i = len(a)
        a.append((a[i - 1] * a[i - 2]) % 26)
        b.append((b[i - 1] + b[i - 2]) % 26)
        i += 1

    if cmd == "1":
        print(affine_recur.affine_recurs_enc(st, a, b))
    elif cmd == "2":
        print(affine_recur.affine_recurs_dec(st, a, b))
    else:
        print("Unknown command")


def decode_affine_manage():
    """This function is used to manage the decoding of affine cipher"""
    cmd = input("Input the ciphertext:\n")
    print(decode_affine.decode_affine(cmd))
