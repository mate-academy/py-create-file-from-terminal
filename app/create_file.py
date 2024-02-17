import os
import sys
from datetime import datetime


def create_directory(directory: str) -> None:
    if os.path.exists(directory) is not True:
        os.makedirs(directory)


def create_file(file_name: str) -> None:
    mode_file = "w" if not os.path.exists(file_name) else "a"
    line_number = 1
    with open(file_name, mode_file) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if mode_file == "w":
            file.write(f"{timestamp}\n")
        else:
            file.write(f"\n{timestamp}\n")
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} Line{line_number} {content}\n")
            line_number += 1


if "-d" in sys.argv and "-f" in sys.argv:
    dir_index = sys.argv.index("-d") + 1
    file_index = sys.argv.index("-f") + 1
    file_name = sys.argv[file_index]
    if sys.argv[1] == "-d" and "-f" in sys.argv:
        directory_path = os.path.join(*sys.argv[dir_index:file_index - 1])
        file_url = os.path.join(directory_path, file_name)
        create_directory(directory_path)
        create_file(file_url)

    elif sys.argv[1] == "-f" and "-d" in sys.argv:
        directory = os.path.join(*sys.argv[dir_index:])
        create_file(file_name)
        create_directory(directory)

else:
    if sys.argv[1] == "-d":
        dir_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[dir_index:])
        create_directory(directory)

    elif sys.argv[1] == "-f":
        file_index = sys.argv.index("-f") + 1
        file_name = sys.argv[file_index]
        create_file(file_name)
