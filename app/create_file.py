import os
import sys
from datetime import datetime


def parse_arguments(argv: str) -> str | None:
    i = 1
    dirs = []
    filename = None
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            i += 1
            while (i < len(sys.argv)) and not sys.argv[i].startswith("-"):
                dirs.append(sys.argv[i])
                i += 1
            continue
        elif sys.argv[i] == "-f":
            filename = sys.argv[i + 1]
            i += 2
            continue
        i += 1
    return dirs, filename


def build_path(dirs: list, filename: str) -> str | bytes:
    path = os.path.join(*dirs) if dirs else ""
    if path:
        os.makedirs(path, exist_ok=True)

    return os.path.join(path, filename)


def write_content(full_path: str) -> None:
    line_number = 1
    file_exists = os.path.exists(full_path)

    with open(full_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}]\n")

        while True:
            user_input = input("Enter content line: ")

            if user_input.lower() == "stop":
                break

            file.write(f"{line_number}. {user_input}\n")
            line_number += 1

        line_number += 1


def create_file() -> None:
    dirs, filename = parse_arguments(sys.argv)
    full_path = build_path(dirs, filename)
    write_content(full_path)
