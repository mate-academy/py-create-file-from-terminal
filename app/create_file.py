import sys
import os
import datetime
from typing import List


def create_directory(path_parts: List[str]) -> None:
    dir_path = os.path.join(*path_parts)
    os.makedirs(dir_path, exist_ok=True)
    print(f"Directory created at: {dir_path}")


def create_file(file_path: str, content_lines: List[str]) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(f"{timestamp}\n")

        for index, line in enumerate(content_lines, 1):
            f.write(f"{index} {line}\n")


def get_file_content() -> List[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file.py\n [-d <directories>] [-f <filename>]")  # noqa: E501
        sys.exit(1)

    dir_parts = []
    file_name = None
    flag_d = False
    flag_f = False

    args = sys.argv[1:]
    while args:
        arg = args.pop(0)
        if arg == "-d":
            flag_d = True
            while args and not args[0].startswith("-"):
                dir_parts.append(args.pop(0))
        elif arg == "-f":
            flag_f = True
            if args:
                file_name = args.pop(0)
        else:
            print(f"Unknown argument: {arg}")
            sys.exit(1)

    if flag_d:
        create_directory(dir_parts)

    if flag_f and file_name:
        file_path = os.path.join(*dir_parts, file_name) if dir_parts else file_name  # noqa: E501

        content_lines = get_file_content()
        create_file(file_path, content_lines)
        print(f"Content added to {file_path}")


if __name__ == "__main__":
    main()
