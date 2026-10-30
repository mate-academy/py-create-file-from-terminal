import os
import sys
from datetime import datetime


def get_directories(args: list[str]) -> listif "-d" not in args:
        return []

    d_index = args.index("-d")

    if "-f" in args:
        f_index = args.index("-f")

        if d_index < f_index:
            return args[d_index + 1:f_index]

    return args[d_index + 1:]


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

    content = [timestamp]

    for index, line in enumerate(lines, start=1):
        content.append(f"{index} {line}")

    file_exists = (
        os.path.exists(file_path)
        and os.path.getsize(file_path) > 0
    )

    with open(file_path, "a") as file:
        if file_exists:
            file.write("\n\n")

        file.write("\n".join(content))


def main() -> None:
    args = sys.argv[1:]

    directories = get_directories(args)

    if directories:
        directory_path = os.path.join(*directories)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = ""

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
