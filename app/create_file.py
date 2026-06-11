import sys
import os
from datetime import datetime


def write_content_to_file(file_path: str) -> None:
    content_lines = []
    while True:
        new_string = input("Enter content line: ")
        if new_string == "stop":
            break
        content_lines.append(new_string)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prepared_lines = [timestamp]

    for index, line in enumerate(content_lines, start=1):
        prepared_lines.append(f"{index} {line}")

    file_has_content = (os.path.exists(file_path)
                        and os.path.getsize(file_path) > 0)

    with open(file_path, "a") as file:
        if file_has_content:
            file.write("\n")

        file.write("\n".join(prepared_lines))
        file.write("\n")


args = sys.argv[1:]

dir_path = ""

if "-d" in args:
    d_index = args.index("-d")
    dir_parts = args[d_index + 1:]

    if "-f" in dir_parts:
        f_inside_dir_index = dir_parts.index("-f")
        dir_parts = dir_parts[:f_inside_dir_index]

    dir_path = os.path.join(*dir_parts)
    os.makedirs(dir_path, exist_ok=True)

if "-f" in args:
    f_index = args.index("-f")
    file_name = args[f_index + 1]

    if dir_path:
        file_path = os.path.join(dir_path, file_name)
    else:
        file_path = file_name

    write_content_to_file(file_path)
