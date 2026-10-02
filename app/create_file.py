import os
import sys
from datetime import datetime


def create_directories(directories: list) -> str:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def get_content_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def write_content(file_path: str, lines: list) -> None:
    title = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as source_file:
        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            source_file.write("\n")
        source_file.write(title + "\n")
        for number, item in enumerate(lines, start=1):
            source_file.write(f"{number} {item}\n")


if "-d" in sys.argv and "-f" in sys.argv:
    dir_flag_index = sys.argv.index("-d")
    file_flag_index = sys.argv.index("-f")
    file_name = sys.argv[file_flag_index + 1]
    if dir_flag_index < file_flag_index:
        directories = sys.argv[dir_flag_index + 1:file_flag_index]
    else:
        directories = sys.argv[dir_flag_index + 1:]
    directories_path = create_directories(directories)
    file_path = os.path.join(directories_path, file_name)
    lines = get_content_lines()
    write_content(file_path, lines)
elif "-d" in sys.argv:
    dir_flag_index = sys.argv.index("-d")
    directories = sys.argv[dir_flag_index + 1:]
    create_directories(directories)
elif "-f" in sys.argv:
    file_flag_index = sys.argv.index("-f")
    file_name = sys.argv[file_flag_index + 1]
    lines = get_content_lines()
    write_content(file_name, lines)
