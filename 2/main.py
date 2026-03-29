"""Main file"""

import manage

command = input("Hello! Choose a command:\n| to use ciphers - 1 | for cryptanalysis - 2 |\n")
if command == "1":
    start = input("Choose a command:\n| hill - 1 | hill_recur - 2 |\n")
    if start == "1":
        manage.hill_manage()
    elif start == "2":
        manage.hill_recur_manage()
    else:
        print("Unknown command")

elif command == "2":
    cmd = input("Choose a command for decode:\n| hill - 1 | hill_recur - 2 |\n")
    if cmd == "1":
        manage.decode_hill_manage()
    elif cmd == "2":
        manage.decode_hill_recur_manage()
    else:
        print("Unknown command")

else:
    print("Unknown command")
