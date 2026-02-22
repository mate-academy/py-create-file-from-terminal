import os
import sys
from datetime import datetime


def parse_args(args: list) -> list | str | None:
    directories: list[str] = []
    filename: str | None = None

    if "-d" in args:
        d_index = args.index("-d")

        if "-f" in args:
            f_index = args.index("-f")
            directories = args[d_index + 1:f_index]
        else:
            directories = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")

        if f_index + 1 < len(args):
            filename = args[f_index + 1]

    return directories, filename


def create_directory(path_parts: list) -> str:
    if not path_parts:
        return ""

    path = os.path.join(*path_parts)

    os.makedirs(path, exist_ok=True)

    return path


def get_content() -> list:
    lines: list[str] = []
    counter = 1

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        lines.append(f"{counter} {line}")

        counter += 1

    return lines


def timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def write_file(
    directory: str,
    filename: str,
    lines: list,
) -> None:

    filepath = filename

    if directory:
        filepath = os.path.join(directory, filename)

    file_exists = os.path.exists(filepath)

    with open(filepath, "a", encoding="utf-8") as file:

        if file_exists:
            file.write("\n")

        file.write(timestamp() + "\n")

        for line in lines:
            file.write(line + "\n")


def main() -> None:
    args = sys.argv[1:]

    directories, filename = parse_args(args)

    directory_path = create_directory(directories)

    if filename:
        lines = get_content()

        write_file(directory_path, filename, lines)


if __name__ == "__main__":
    main()
