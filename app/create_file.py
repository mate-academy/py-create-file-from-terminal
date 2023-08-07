from __future__ import annotations

import sys
import os
from datetime import datetime
from typing import Union


def make_path(cmd_arguments: list[Union[bytes, str]]) -> tuple[Union[bytes, str], Union[bytes, str], Union[bytes, str]]:
    path, filename, filepath = " ", " ", " "
    cmd_arguments.pop(0)  # delete executed filename from arguments
    if "-f" in cmd_arguments:
        filename = cmd_arguments[cmd_arguments.index("-f") + 1]
        cmd_arguments.pop(cmd_arguments.index("-f"))
        cmd_arguments.pop(cmd_arguments.index(filename))
    if "-d" in cmd_arguments:
        cmd_arguments.pop(cmd_arguments.index("-d"))
        path = os.path.join(*cmd_arguments)
    if path == " ":
        filepath = filename
    else:
        filepath = os.path.join(path, filename)
    return path, filename, filepath


def create_file() -> None:
    path, filename, filepath = make_path(sys.argv)
    if filename == " ":
        os.makedirs(path, exist_ok=True)
    else:
        if path != " ":
            os.makedirs(path, exist_ok=True)
        with open(filepath, "w") as source_file:
            current_time = datetime.now()
            source_file.write(str(current_time.strftime("%Y-%m-%d %H:%M:%S")))

            while True:
                user_cmd = input("Enter content line:")
                if user_cmd == "stop":
                    break
                source_file.write("\n" + user_cmd)


if __name__ == "__main__":
    create_file()
