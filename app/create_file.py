import os
import sys
from datetime import datetime


def get_directories(args: list[str]) -> listif "-d" not in args:
        return []

    d_index = args.index("-d")

    directory_args = []

    for argument in args[d_index + 1:]:
        if argument == "-f":
            break

        directory_args.append(argument)

    return directory_args


def get_file_name(args: list[str]) -> str:
    if "-f" not in args:
        return ""

    f_index = args.index("-f")

    return args[f_index + 1]


def get_content() -> listlines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(line)

    return lines


def write_content(file_path: str, lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    block = [timestamp]

    for index, line in enumerate(lines, start=1):
        block.append(f"{index} {line}")

    has_content = (
        os.path.exists(file_path)
        and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a") as file:
        if has_content:
            file.write("\n\n")

        file.write("\n".join(block))


def main() -> None:
    args = sys.argv[1:]

    directories = get_directories(args)

    directory_path = ""

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)

    file_name = get_file_name(args)

    if not file_name:
        return

    if directory_path:
        file_path = os.path.join(directory_path, file_name)
    else:
        file_path = file_name

    lines = get_content()

    write_content(file_path, lines)


if __name__ == "__main__":
    main()
