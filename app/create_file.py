import os
import sys
from datetime import datetime


def create_directory(dir_parts: list[str]) -> str:
    path = os.path.join(*dir_parts)
    os.makedirs(path, exist_ok=True)
    return path


def create_file_with_content(file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_number = 1

        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1

        file.write("\n")


def handle_arguments(argv: list[str]) -> None:
    if "-d" in argv and "-f" not in argv:
        dir_index = argv.index("-d") + 1
        dir_parts = argv[dir_index:]
        create_directory(dir_parts)

    elif "-f" in argv and "-d" not in argv:
        file_index = argv.index("-f") + 1
        file_name = argv[file_index]
        create_file_with_content(file_name)

    elif "-d" in argv and "-f" in argv:
        dir_index = argv.index("-d") + 1
        file_index = argv.index("-f") + 1

        if dir_index < file_index:
            dir_parts = argv[dir_index:file_index - 1]
            file_name = argv[file_index]
        else:
            file_name = argv[file_index]
            dir_parts = argv[dir_index:]

        dir_path = create_directory(dir_parts)
        file_path = os.path.join(dir_path, file_name)
        create_file_with_content(file_path)
