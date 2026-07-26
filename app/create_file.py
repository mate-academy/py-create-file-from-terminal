import sys
import os
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    dir_path = ""
    file_name = ""

    if "-d" in args:
        d_index = args.index("-d")
        path_parts = []
        for arg in args[d_index + 1:]:
            if arg == "-f":
                break
            path_parts.append(arg)
        dir_path = os.path.join(*path_parts) if path_parts else ""

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    return dir_path, file_name


def get_content_from_user() -> list:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_to_file(full_path: str, content: list) -> None:
    file_exists = os.path.exists(full_path)
    file_is_not_empty = file_exists and os.path.getsize(full_path) > 0

    with open(full_path, "a") as output_file:
        if file_is_not_empty:
            output_file.write("\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        output_file.write(f"{timestamp}\n")
        for index, line in enumerate(content, start=1):
            output_file.write(f"{index} {line}\n")


def main() -> None:
    dir_path, file_name = parse_arguments(sys.argv[1:])

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        full_path = os.path.join(dir_path, file_name)
        content = get_content_from_user()
        if content:
            write_to_file(full_path, content)


if __name__ == "__main__":
    main()
