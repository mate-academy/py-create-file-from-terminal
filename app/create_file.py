import sys
import os
from datetime import datetime


def parse_args(argv: list[str]) -> tuple:
    dirs = []
    file_name = None

    for i, arg in enumerate(argv):
        if arg == "-d":
            for index in range(i + 1, len(argv)):
                next_arg = argv[index]
                if next_arg.startswith("-"):
                    break
                dirs.append(next_arg)

        if arg == "-f":
            if i + 1 < len(argv) and not argv[i + 1].startswith("-"):
                file_name = argv[i + 1]

    return (dirs, file_name)


def ensure_dirs(dirs: list) -> str:
    if not dirs:
        return "."

    full_path_dir = os.path.join(*dirs)
    os.makedirs(full_path_dir, exist_ok=True)

    return full_path_dir


def write_content(file_name: str) -> None:
    content_lines = []

    while True:
        new_line = input("Enter content line: ")

        if new_line == "stop":
            break
        content_lines.append(new_line)

    if content_lines:
        needs_separator = (os.path.exists(file_name)
                           and os.path.getsize(file_name) > 0)
        current_data = datetime.now()

        with open(file_name, "a", encoding="utf-8") as new_file:

            if needs_separator:
                new_file.write("\n")

            new_file.write(current_data.strftime("%Y-%m-%d %H:%M:%S\n"))

            for i, line in enumerate(content_lines, start=1):
                new_file.write(f"{i} {line}\n")


def main() -> None:
    dirs, file_name = parse_args(sys.argv[1:])

    if not file_name:
        print("You need to write file name")
        return

    full_file_path = os.path.join(ensure_dirs(dirs), file_name)

    write_content(full_file_path)
