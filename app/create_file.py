import os
import sys
from datetime import datetime
from typing import Union


def get_directory_path(args: list) -> Union[str | None]:
    if "-d" in args:
        start_index = args.index("-d") + 1
        end_index = args.index("-f") if "-f" in args else len(args)
        return str(os.path.join(*args[start_index:end_index]))
    return None


def get_file_name(args: list) -> Union[str, None]:
    return args[-1] if "-f" in args else None


def create_file(file_path: Union[str, None]) -> None:
    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        while (content_line := input("Enter content line: ")) != "stop":
            file.write(f"{line_number} {content_line}\n")
            line_number += 1


arguments = sys.argv
directory_path = get_directory_path(arguments)
file_name = get_file_name(arguments)

if directory_path and file_name:
    os.makedirs(directory_path)
    create_file(os.path.join(directory_path, file_name))
elif directory_path:
    os.makedirs(directory_path)
elif file_name:
    create_file(file_name)
