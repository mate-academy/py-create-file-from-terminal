import sys
import os
from datetime import datetime


def create_file_with_content(path: str) -> None:
    line_number = 1
    content_lines = []

    while True:
        content_line = input("Enter content line: ")
        if content_line == "stop":
            break
        content_lines.append(f"{line_number} {content_line}")
        line_number += 1

    with open(path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if os.stat(path).st_size != 0:
            file.write("\n\n")
        file.write(timestamp + "\n")
        file.write("\n".join(content_lines))


def create_file_path(dir_path: str) -> None:

    file_name = sys.argv[file_index + 1]
    file_path = os.path.join(dir_path, file_name)
    create_file_with_content(file_path)


if "-d" in sys.argv and "-f" in sys.argv:
    dir_index = sys.argv.index("-d")
    file_index = sys.argv.index("-f")
    if dir_index < file_index:
        directory_path = os.path.join(*sys.argv[dir_index + 1:file_index])

        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        create_file_path(directory_path)
    else:
        directory_path = os.path.join(*sys.argv[dir_index + 1:])
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        create_file_path(directory_path)

elif "-d" in sys.argv:
    directory_flag_index = sys.argv.index("-d")
    directory_path = os.path.join(*sys.argv[directory_flag_index + 1:])

    os.makedirs(directory_path)

elif "-f" in sys.argv:
    file_flag_index = sys.argv.index("-f")
    file_name = sys.argv[file_flag_index + 1]

    file_path = os.path.join(os.getcwd(), file_name)

    create_file_with_content(file_path)
