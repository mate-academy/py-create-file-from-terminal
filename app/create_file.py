import sys
import os
from datetime import datetime


def create_file(file_name: str, path_parts: list) -> None:
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = date_time
    line_number = 1
    while True:
        message = input("Enter content line: ")
        if message == "stop":
            break
        else:
            content += f"\n{str(line_number)} {message}"
            line_number += 1

    parent_path = get_path(path_parts)
    file_path = os.path.join(parent_path, file_name)
    is_exist = os.path.exists(file_path)

    with open(file_path, "a") as file:
        if is_exist:
            file.write("\n\n")
        file.write(f"{content}")


def create_dir(path_parts: list) -> None:
    parent_path = get_path(path_parts)
    os.makedirs(parent_path, exist_ok=True)


def get_path(path_parts: list) -> str:
    parent_path: str = os.getcwd()
    for folder in path_parts:
        parent_path = os.path.join(parent_path, folder)
    return parent_path


def main() -> None:
    args = sys.argv[1:]
    if len(args) == 0:
        return
    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")

        if dir_index < file_index:
            path_parts = args[dir_index + 1:file_index]
            file_name = args[file_index + 1]
        else:
            path_parts = args[dir_index + 1:]
            file_name = args[file_index + 1:dir_index][0]

        create_dir(path_parts)
        create_file(file_name, path_parts)

    elif "-d" in args:
        dir_index = args.index("-d")
        path_parts = args[dir_index + 1:]

        create_dir(path_parts)

    elif "-f" in args:
        dir_index = args.index("-f")
        file_name = args[dir_index + 1]

        create_file(file_name, [])


if __name__ == "__main__":
    main()
