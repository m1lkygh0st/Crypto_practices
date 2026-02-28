"""File: main.py"""

import manage

command = input("Hello! Choose a command:\n| to use ciphers - 1 | for cryptanalysis - 2 |\n")
if command == "1":
    start = input("Choose a command:\n| simp_sub - 1 | affine - 2 | affine_recur - 3 |\n")
    if start == "1":
        manage.simp_sub_manage()
    elif start == "2":
        manage.affine_manage()
    elif start == "3":
        manage.affine_recur_manage()
    else:
        print("Unknown command")

elif command == "2":
    cmd = input("Choose a command for decode:\n| simp_sub - 1 | affine - 2 | affine_recur - 3 |\n")
    if cmd == "2":
        manage.decode_affine_manage()
    elif cmd in {"1", "3"}:
        print("This section is currently under development")
    else:
        print("Unknown command")

else:
    print("Unknown command")
