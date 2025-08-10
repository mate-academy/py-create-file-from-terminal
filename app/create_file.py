import datetime
import os
import sys


def create_directory(path_parts: list) -> None:
    if not path_parts:
        return
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)


def create_file(file_name: str, path_parts: list = None) -> None:
    if not file_name:
        return
    if path_parts is None:
        path_parts = []
    if path_parts:
        full_path = os.path.join(*path_parts, file_name)
    else:
        full_path = file_name
    with open(full_path, "a") as file:
        file.write(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
        )
        content = ""
        line_number = 0
        while True:
            line = input("Enter content: ")
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
        file_name = args[file_index + 1]
        if dir_index < file_index:
            path_parts = args[dir_index + 1:file_index]
        else:
            path_parts = args[dir_index + 1:]
    elif "-d" in args:
        dir_index = args.index("-d")
        path_parts = args[dir_index + 1:]
        file_name = None
    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        path_parts = None
    else:
        path_parts = []
        file_name = None
    create_directory(path_parts)
    create_file(file_name, path_parts)


if __name__ == "__main__":
    main()
