import datetime

import os

import sys


def create_directory(path_parts: list) -> None:
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)


def create_file(file_name: str, path_parts: list = None) -> None:
    if path_parts:
        create_directory(path_parts)
        full_path = os.path.join(os.path.join(*path_parts), file_name)
    else:
        full_path = file_name
    with (open(full_path, "a") as file):
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        content = ""
        line_number = 0
        while True:
            line = input("Enter content content: ")
            if line == "stop":
                content += "\n"
                break
            line_number += 1
            content += f"{line_number} {line} \n"
        file.write(content)


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        if dir_index < file_index:
            path_parts = args[dir_index + 1:file_index]
            file_name = args[file_index + 1]
            create_directory(path_parts)
            create_file(file_name, path_parts)
        else:
            path_parts = args[dir_index + 1:]
            file_name = args[file_index + 1]
            print(file_name, path_parts)
            create_directory(path_parts)
            create_file(file_name, path_parts)
    elif "-d" in args and "-f" not in args:
        create_directory(args[1:])
    elif "-f" in args and "-d" not in args:
        create_file(args[args.index("-f") + 1])


print(__name__)
if __name__ == "__main__":
    main()
