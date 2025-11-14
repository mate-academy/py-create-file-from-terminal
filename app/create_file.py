import sys
import os
from datetime import datetime


def process_input() -> list:
    args_list = []
    for arg in sys.argv:
        args_list.append(arg)
    return args_list[1:]


def current_date() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def process_file(args_list: list) -> None:

    if args_list[0] == "-b":
        i = 1
        path_parts = []
        while args_list[i] != "-f":
            path_parts.append(args_list[i])
            i += 1
        path_to_file = os.path.join(*path_parts, args_list[- 1])

    else:
        path_to_file = args_list[1]

    directory = os.path.dirname(path_to_file)
    if directory:
        os.makedirs(directory, exist_ok=True)

    with open(path_to_file, "w") as file:
        line_counter = 1
        file.write(current_date() + "\n")
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(f"{line_counter} {user_input}\n")
            line_counter += 1


process_file(process_input())
