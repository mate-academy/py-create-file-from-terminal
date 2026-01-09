import sys
import os
from datetime import datetime
from typing import List


def get_directory_path(args: List[str]) -> str:
    if "-d" not in args:
        return ""
    d_index = args.index("-d")
    end_index = len(args)
    if "-f" in args:
        f_index = args.index("-f")
        if f_index > d_index:
            end_index = f_index
    dir_parts = args[d_index + 1:end_index]
    if dir_parts:
        return os.path.join(*dir_parts)
    return ""


def get_filename(args: List[str]) -> str:
    if "-f" not in args:
        return ""

    f_index = args.index("-f")
    if f_index + 1 < len(args):
        return args[f_index + 1]
    return ""


def create_directory(path: str) -> None:
    if path:
        os.makedirs(path, exist_ok=True)


def get_user_content() -> List[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_to_file(file_path: str, content_lines: List[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    text_to_write = f"{timestamp}\n"
    for i, line in enumerate(content_lines, 1):
        text_to_write += f"{i} {line}\n"
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        text_to_write = "\n" + text_to_write
    with open(file_path, "a", encoding="utf-8") as target_file:
        target_file.write(text_to_write)


def main() -> None:
    args = sys.argv[1:]
    dir_path = get_directory_path(args)
    file_name = get_filename(args)
    create_directory(dir_path)
    if file_name:
        full_file_path = file_name
        if dir_path:
            full_file_path = os.path.join(dir_path, file_name)
        user_content = get_user_content()
        write_to_file(full_file_path, user_content)
