"""Main module"""

import manage


start = input(
    "Hello! Choose a command:\n| to use ciphers - 1 | for cryptanalysis - 2 |\n"
)
if start == "1":
    command = input("Hello! Choose a command:\n| v1 - 1 | v2 - 2 | v3 - 3 |\n")

    cmd = input("Choose a command:\n| encode - 1 | decode - 2 |\n")
    text = input("Input text: ")
    key = input("Input key: ")

    if command == "1":
        manage.v1_manage(text, key, cmd)
    elif command == "2":
        manage.v2_manage(text, key, cmd)
    elif command == "3":
        manage.v3_manage(text, key, cmd)
    else:
        print("Unknown command")

elif start == "2":
    command = input("Hello! Choose a command:\n| v1 - 1 | v2 - 2 | v3 - 3 |\n")
    if command == "1":
        manage.v11_manage()
    elif command == "2":
        manage.v22_manage()
    elif command == "3":
        manage.v33_manage()
    else:
        print("Unknown command")
else:
    print("Unknown command")
