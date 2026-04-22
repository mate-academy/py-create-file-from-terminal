import sys
import os
from datetime import datetime


def get_flag_index(flag: str) -> int | None:
    if flag in sys.argv:
        return sys.argv.index(flag)
    return None


def get_path_list(d_index: int) -> list:
    path_list = []
    for i in range(d_index + 1, len(sys.argv)):
        if sys.argv[i].startswith("-"):
            break
        path_list.append(sys.argv[i])
    return path_list


def create_directory(path_list: list) -> None:
    if not path_list:
        return
    os.makedirs(os.path.join(*path_list), exist_ok=True)


def get_content() -> list:
    content = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(line)
    return content


def write_to_file(filepath: str, content: list) -> None:
    is_file_empty = (not os.path.exists(filepath)
                     or os.path.getsize(filepath) == 0)
    prefix = "" if is_file_empty else "\n"

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a") as source_file:
        source_file.write(f"{prefix}{timestamp}\n")
        for number, line in enumerate(content, start=1):
            source_file.write(f"{number} {line}\n")


d_index = get_flag_index("-d")
f_index = get_flag_index("-f")

path_list = []
if d_index is not None:
    path_list = get_path_list(d_index)
    if path_list:
        create_directory(path_list)

if f_index is not None:
    if f_index + 1 < len(sys.argv):
        filename = sys.argv[f_index + 1]
        filepath = (
            os.path.join(*path_list, filename) if path_list else filename
        )
        open(filepath, "a").close()
        content = get_content()
        write_to_file(filepath, content)
