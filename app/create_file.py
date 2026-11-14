import os
import sys
from datetime import datetime


def get_path_parts(
    args: list[str],
    flag: str,
) -> list[str]:
    if flag not in args:
        return []
    parts = []
    for item in args[args.index(flag) + 1:]:
        if item in ("-d", "-f"):
            break
        parts.append(item)
    return parts


def read_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            return lines
        lines.append(line)


def write_file(
    file_path: str,
    lines: list[str],
) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    is_not_empty = (
        os.path.exists(file_path) and os.path.getsize(file_path) > 0
    )
    with open(file_path, "a") as file:
        if is_not_empty:
            file.write("\n")
        file.write(timestamp + "\n")
        for number, line in enumerate(lines, start=1):
            file.write(f"{number} {line}\n")


def main() -> None:
    args = sys.argv[1:]
    directories = get_path_parts(args, "-d")
    file_parts = get_path_parts(args, "-f")

    directory = os.path.join(*directories) if directories else ""
    if directory:
        os.makedirs(directory, exist_ok=True)

    if not file_parts:
        return

    file_path = os.path.join(directory, file_parts[0])
    write_file(file_path, read_content())


main()
