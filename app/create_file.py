import sys
import os
from datetime import datetime
from typing import Any


def create_directory(path_parts: str) -> Any:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_name, "a") as file:
        file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content = input(str(f"Enter content line: {line_number} "))
            if content == "stop":
                break
            file.write(f"{line_number} Line{line_number}"
                       f" + {"".join(content)} + \n")
            line_number += 1


def main() -> None:
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        if "-f" in sys.argv:
            f_index = sys.argv.index("-f")
            dir_path = create_directory(str(sys.argv[d_index + 1:f_index]))
            file_name = sys.argv[f_index + 1]
        else:
            create_directory(str(sys.argv[d_index + 1:]))
            return
    elif "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        dir_path = ""
    else:
        return

    file_path = os.path.join(dir_path, file_name)
    create_file(file_path)
