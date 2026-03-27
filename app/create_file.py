import os
import sys
from datetime import datetime


def parse_arguments(args: list) -> tuple:
    d_idx = args.index("-d") if "-d" in args else None
    f_idx = args.index("-f") if "-f" in args else None

    dir_path = ""
    if d_idx is not None:
        end_idx = f_idx if (f_idx is not None and f_idx > d_idx) else len(args)
        parts = args[d_idx + 1:end_idx]
        if parts:
            dir_path = os.path.join(*parts)

    file_name = ""
    if f_idx is not None and f_idx + 1 < len(args):
        file_name = args[f_idx + 1]

    return dir_path, file_name


def get_user_content() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(full_path: str, lines: list) -> None:
    file_exists = os.path.exists(full_path)
    needs_newline = file_exists and os.path.getsize(full_path) > 0

    with open(full_path, "a") as file:
        if needs_newline:
            file.write("\n")

        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"{timestamp}\n")

        for i, line in enumerate(lines, start=1):
            file.write(f"{i} {line}\n")


def create_file() -> None:
    dir_path, file_name = parse_arguments(sys.argv[1:])

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        content = get_user_content()
        full_path = os.path.join(dir_path, file_name)
        write_to_file(full_path, content)


if __name__ == "__main__":
    create_file()
