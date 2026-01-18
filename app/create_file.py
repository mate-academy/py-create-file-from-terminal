import sys
import os
from datetime import datetime
from itertools import groupby


def create_file(*args) -> None:

    def parse_args(arguments: tuple) -> [list, list]:
        arguments = arguments[1:]
        arguments = [list(group) for k, group in
                     groupby(arguments, lambda x: x in ("-f", "-d"))]
        d_args = []
        f_args = []

        for index in range(len(arguments)):
            if arguments[index] == ["-d"]:
                d_args = arguments[index + 1]
            if arguments[index] == ["-f"]:
                f_args = arguments[index + 1]

        return d_args, f_args

    d_args, f_args = parse_args(args)

    full_file_path = ""

    if d_args != []:
        print(d_args)
        directory_path = os.path.join(*d_args)
        os.makedirs(directory_path)

    if f_args != []:
        if d_args != []:
            full_file_path = os.path.join(directory_path, f_args[0])
        else:
            full_file_path = f_args[0]
        with open(full_file_path, "a") as file:
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
