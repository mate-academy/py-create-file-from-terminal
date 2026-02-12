import sys
import os
from datetime import datetime


def get_directory_and_file_from_args(args: str) -> tuple:
    dir_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_parts = args[d_index + 1: f_index]
        else:
            dir_parts = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    return dir_parts, file_name


def create_directory(dir_parts: list) -> str:
    if dir_parts:
        path = os.path.join(*dir_parts)
        os.makedirs(path, exist_ok=True)
        return path
    return ""


def get_content_from_user() -> list:
    lines = []
    counter = 1

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1

    return lines


def write_to_file(file_path: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_block = timestamp + "\n"
    content_block += "\n".join(lines)
    content_block += "\n"

    if os.path.exists(file_path):
        content_block = "\n" + content_block

    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content_block)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("No arguments provided")
        return

    dir_parts, file_name = get_directory_and_file_from_args(args)
    dir_path = create_directory(dir_parts)

    if file_name:
        if dir_path:
            file_path = os.path.join(dir_path, file_name)
        else:
            file_path = file_name
        write_to_file(file_path, lines=get_content_from_user())

    elif dir_path:
        print("Directories created successfully")


if __name__ == "__main__":
    main()
