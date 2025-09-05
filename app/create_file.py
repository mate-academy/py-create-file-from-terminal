import os
import sys
from datetime import datetime


def create_file() -> str:
    list_arg = sys.argv
    if "-d" in list_arg and "-f" in list_arg:
        flag_d = list_arg.index("-d")
        flag_f = list_arg.index("-f")
        os.makedirs(os.path.join(*list_arg[flag_d + 1:flag_f]), exist_ok=True)
        path = os.path.join(*list_arg[flag_d + 1:flag_f], list_arg[flag_f + 1])
        return path
    if "-d" in list_arg and "-f" not in list_arg:
        flag_d = list_arg.index("-d")
        os.makedirs(os.path.join(*list_arg[flag_d + 1:]), exist_ok=True)
    if "-f" in list_arg and "-d" not in list_arg:
        flag_f = list_arg.index("-f")
        path = os.path.join(list_arg[flag_f + 1])
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
