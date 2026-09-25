import os
import sys

from datetime import datetime
from typing import TextIO


def get_user_input() -> dict | None:
    if "-f" not in sys.argv and "-d" not in sys.argv:
        print("you should provide '-d' or '-f' flag")
        sys.exit(1)

    user_arguments = {
        "file_name": "",
        "dir_path": ""
    }

    if "-f" in sys.argv:
        file_command_idx = sys.argv.index("-f")
        if (len(sys.argv[file_command_idx + 1:]) >= 1
                and "-" not in sys.argv[file_command_idx + 1]):
            user_arguments["file_name"] = sys.argv[file_command_idx + 1]

    if "-d" in sys.argv:
        dir_command_inx = sys.argv.index("-d")
        for arg in sys.argv[dir_command_inx + 1:]:
            if "-" in arg:
                break
            user_arguments["dir_path"] = os.path.join(
                user_arguments["dir_path"], arg
            )
    return user_arguments


def write_content(file_object: TextIO) -> None:
    file_object.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    user_input = input("Enter content line: ")
    numerator = 1
    while user_input != "stop":
        file_object.write(str(numerator) + " " + user_input + "\n")
        numerator += 1
        user_input = input("Enter content line: ")


def create_file() -> None:
    user_data = get_user_input()
    user_path, user_file = user_data["dir_path"], user_data["file_name"]

    if not user_path and not user_file:
        print("no files and no dirs")
        sys.exit(2)

    if user_path:
        os.makedirs(user_path, exist_ok=True)

    if user_file:
        current_path = os.path.join(user_path, user_file)

        if os.path.exists(current_path):
            with open(current_path, "a") as file:
                file.write("\n")
                write_content(file)
        elif not os.path.exists(current_path):
            with open(current_path, "a") as file:
                write_content(file)


create_file()
