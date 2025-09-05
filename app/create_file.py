import os
import sys
from datetime import datetime


def create_file() -> str:
    list_arg = sys.argv[1:]
    flag_d = list_arg.index("-d")
    flag_f = list_arg.index("-f")
    dir_arg = list_arg[flag_d + 1:flag_f]
    file_arg = list_arg[flag_f + 1]
    if not dir_arg:
        raise ValueError("A directory name is expected after -d")
    if not file_arg:
        raise ValueError("A file name is expected after -f")
    if (("-d" in list_arg and "-f" in list_arg)
            or ("-f" in list_arg and "-d" in list_arg)):
        os.makedirs(os.path.join(*dir_arg), exist_ok=True)
        path = os.path.join(*dir_arg, file_arg)
        return path
    if "-d" in list_arg and "-f" not in list_arg:
        os.makedirs(os.path.join(*list_arg[flag_d + 1:]), exist_ok=True)
    if "-f" in list_arg and "-d" not in list_arg:
        path = os.path.join(os.getcwd(), file_arg)
        return path


def write_content(path: str) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(path, "a") as file:
        if os.path.exists(path) and os.path.getsize(path):
            file.write("\n")
        file.write(current_time + "\n")
        page_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{page_number} {content}\n")
            page_number += 1
