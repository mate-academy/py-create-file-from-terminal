import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    return str(os.path.join(*directories))


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(filename: str) -> None:
    with open(filename, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_num = 1
        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(f"{line_num} {user_input}\n")
        file.write("\n")


def main(args: list[str]) -> None:
    try:
        dir_index = args.index("-d")
    except ValueError:
        dir_index = None

    try:
        file_index = args.index("-f")
    except ValueError:
        file_index = None

    if dir_index is not None:
        if file_index is not None:
            path = create_path(args[dir_index + 1: file_index])
            create_directory(path)
            create_file(os.path.join(path, args[file_index + 1]))
        else:
            path = create_path(args[dir_index + 1:])
            create_directory(path)
    elif file_index is not None:
        create_file(args[file_index + 1])


if __name__ == "__main__":
    main(sys.argv[1:])
