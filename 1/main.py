"""File: main.py"""

import simp_sub
import affine
import affine_recur

command = input("Hello! Choose 1 to use ciphers or 2 for cryptoanalysis: ")
if command == "1":
    start = input("Choose a command: simp_sub, affine or affine_recurs: ")
    if start == "simp_sub":
        cmd = input("simp_sub: input encode or decode: ")
        st, letters2 = input("input two strings with the space: \n").split()
        if cmd == "encode":
            print(simp_sub.simp_sub_enc(st, letters2))
        elif cmd == "decode":
            print(simp_sub.simp_sub_dec(st, letters2))
        else:
            print("Unknown command")
    elif start == "affine":
        cmd = input("affine: input encode or decode: ")
        ST = input("input string: \n")
        AA, BB = map(int, input("input two digits with the space: \n").split())
        if cmd == "encode":
            print(affine.affine_enc(ST, AA, BB))
        elif cmd == "decode":
            print(affine.affine_dec(ST, AA, BB))
        else:
            print("Unknown command")

    elif start == "affine_recurs":
        cmd = input("affine_recurs: input encode or decode: ")
        input_st = input("input string: \n")
        a = list(map(int, input("input two digits with the space: \n").split()))
        b = list(map(int, input("input two digits with the space: \n").split()))

        while len(input_st) > len(a):
            i = len(a)
            a.append((a[i - 1] * a[i - 2]) % 26)
            b.append((b[i - 1] + b[i - 2]) % 26)
            i += 1

        if cmd == "encode":
            print(affine_recur.affine_recurs_enc(input_st, a, b))
        elif cmd == "decode":
            print(affine_recur.affine_recurs_dec(input_st, a, b))
        else:
            print("Unknown command")
    else:
        print("Please choose a command")

elif command == "2":
    print("This section is currently under development")

else:
    print("Unknown command")