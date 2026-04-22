import os
import sys
from datetime import datetime


def create_app() -> None:
    args = sys.argv[1:]
    path_parts: list[str] = []
    file_name = ""

    file_name = parse_arguments(args, file_name, path_parts)
    directory_path = form_path(path_parts)

    if file_name:
        full_file_path = os.path.join(directory_path, file_name)
        content_lines = input_reader()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        write_into_file(content_lines, full_file_path, timestamp)


def input_reader() -> list[str]:
    content_lines = []
    while True:
        user_line = input("Enter content line: ")
        if user_line == "stop":
            break
        content_lines.append(user_line)
    return content_lines


def form_path(path_parts: list[str]) -> str:
    directory_path = "."
    if path_parts:
        directory_path = os.path.join(*path_parts)
        os.makedirs(directory_path, exist_ok=True)
    return directory_path


def parse_arguments(
        args: list[str],
        file_name: str,
        path_parts: list[str]
) -> str:
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                path_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            if i + 1 < len(args):
                file_name = args[i + 1]
            i += 2
        else:
            i += 1
    return file_name


def write_into_file(
        content_lines: list[str],
        full_path: str,
        timestamp: str
) -> None:
    file_exists = os.path.exists(full_path) and os.path.getsize(full_path) > 0

    with open(full_path, "a") as f:
        if file_exists:
            f.write("\n")

        f.write(timestamp + "\n")
        for idx, text in enumerate(content_lines, 1):
            f.write(f"{idx} {text}\n")


if __name__ == "__main__":
    create_app()
