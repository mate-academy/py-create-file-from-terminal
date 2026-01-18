import sys
import os
from datetime import datetime
from itertools import groupby


def create_file(*args) -> None:

    args = args[1:]
    file_name = ""
    if "-f" in args:
        *args, file_name = [list(group) for k, group in
                            groupby(args, lambda x: x == "-f") if not k]
        file_name = file_name[0]

    if "-d" in args:
        *args, directories = [list(group) for k, group in
                              groupby(args, lambda x: x == "-d") if not k]
        os.makedirs(os.path.join(*directories))

    if file_name != "":
        with open(file_name, "a") as file:
            loop_continues = True
            line_number = 1
            file.write(f"{datetime.now().strftime('%Y_%m_%d %H:%M:%S')}\n")
            while loop_continues:
                user_input = input("Enter content line: ")
                if user_input == "stop":
                    loop_continues = False
                    line_number = 1
                    file.write("\n")
                else:
                    file.write(f"{line_number} {user_input}\n")
                    line_number += 1


if __name__ == "__main__":
    create_file(*sys.argv)
