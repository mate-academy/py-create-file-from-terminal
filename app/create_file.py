import os
from sys import argv
from datetime import datetime
from typing import Optional, Tuple


def take_command() -> Tuple[list, Optional[str]]:

    dirs_list = []
    file_name = None
    if "-d" in argv:
        idx = argv.index("-d") + 1
        for arg in argv[idx:]:
            if arg.startswith("-"):
                break
            dirs_list.append(arg)

    if "-f" in argv:
        idx = argv.index("-f")
        if idx + 1 < len(argv):
            file_name = argv[idx + 1]

    return (dirs_list, file_name)


def create_flow(dirs_list: list, file_name: Optional[str]) -> None:
    full_path = None
    dirpath = None

    if file_name:
        if len(dirs_list) > 0:
            full_path = os.path.join(*dirs_list, file_name)
            dirpath = os.path.dirname(full_path)
        else:
            full_path = file_name

    elif file_name is None and len(dirs_list) > 0:
        os.makedirs(os.path.join(*dirs_list), exist_ok=True)
        return

    if dirpath:
        os.makedirs(dirpath, exist_ok=True)

    if full_path is None:
        return

    with open(full_path, "a") as file:
        lines = []
        now = datetime.now()
        formatted = now.strftime("%Y-%m-%d %H:%M:%S")
        if os.path.exists(full_path) and os.path.getsize(full_path) > 0:
            file.write("\n\n")
        file.write(formatted)
        file.write("\n")

        line_text = input("Enter content line: ")
        i = 0
        while line_text != "stop":
            i += 1
            line_text_number = f"{i} {line_text}"
            lines.append(line_text_number)
            line_text = input("Enter content line: ")

        file.write("\n".join(lines))
