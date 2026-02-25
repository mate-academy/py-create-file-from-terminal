import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def read_content() -> list[str]:
    lines = []
    counter = 1

    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1

    return lines


def parse_arguments(arguments: list[str]) -> tuple[list[str], str | None]:
    directory_parts = []
    file_name = None

    if "-d" in arguments:
        d_index = arguments.index("-d")

        # directory arguments end at next flag or end of list
        next_flag_index = len(arguments)
        if "-f" in arguments:
            f_index = arguments.index("-f")
            if f_index > d_index:
                next_flag_index = f_index

        directory_parts = arguments[d_index + 1:next_flag_index]

    if "-f" in arguments:
        f_index = arguments.index("-f")
        if f_index + 1 < len(arguments):
            file_name = arguments[f_index + 1]

    return directory_parts, file_name


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("No arguments provided")
        return

    directory_parts, file_name = parse_arguments(args)

    # Create directories if provided
    dir_path = ""
    if directory_parts:
        dir_path = os.path.join(*directory_parts)
        os.makedirs(dir_path, exist_ok=True)

    # If only -d was passed
    if "-d" in args and "-f" not in args:
        return

    if not file_name:
        print("File name not provided")
        return

    file_path = os.path.join(dir_path, file_name)

    content_lines = read_content()
    timestamp = get_timestamp()

    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write(timestamp + "\n")
        for line in content_lines:
            file.write(line + "\n")


if __name__ == "__main__":
    main()
