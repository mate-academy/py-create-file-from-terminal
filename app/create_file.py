from datetime import datetime
import os
import sys


def path_create(path_parts: list[str]) -> str:
    file_part = ""
    dirs_part = []
    mode = None

    for arg in path_parts:
        if arg == "-f":
            mode = "file"
        elif arg == "-d":
            mode = "dir"
        elif mode == "file":
            file_part = arg
        elif mode == "dir":
            dirs_part.append(arg)

    return os.path.join(*dirs_part, file_part)


def collecting_data() -> list:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    content = [timestamp]
    line_number = 1
    while True:
        text_line = input("Enter content line: ")
        if text_line == "stop":
            break
        content.append(f"{line_number} {text_line}\n")
        line_number += 1

    return content


def writing_file(full_path: str, content: list[str]) -> None:
    with open(full_path, "a") as file:
        if os.path.getsize(full_path):
            file.write("\n")
        file.writelines(content)


cli_args = sys.argv[1:]
path = path_create(cli_args)
dir_path = os.path.dirname(path)
file_name = os.path.basename(path)
if dir_path:
    os.makedirs(dir_path)
if file_name:
    data = collecting_data()
    writing_file(path, data)
