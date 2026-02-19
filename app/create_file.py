import sys
import os
from datetime import datetime


def create_path(directories: list) -> str:
    return os.path.join(*directories)


def make_directories(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def collect_content_lines() -> list:
    lines = []
    while True:
        user_input = input("Enter content line: ")
        if user_input.strip().lower() == "stop":
            break
        lines.append(user_input)
    return lines


def write_content_to_file(filepath: str, lines: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filepath, "a", encoding="utf-8") as file:
        file.write(f"{timestamp}\n")
        for idx, line in enumerate(lines, start=1):
            file.write(f"{idx} {line}\n")
        file.write("\n")


def find_flag_index(args: list, flag: str) -> int | None:
    try:
        return args.index(flag)
    except ValueError:
        return None


def parse_arguments(args: list) -> tuple[list, str | None]:
    directory_path = []
    file_name = None

    d_index = find_flag_index(args, "-d")
    f_index = find_flag_index(args, "-f")

    if d_index is not None:
        i = d_index + 1
        while i < len(args) and not args[i].startswith("-"):
            directory_path.append(args[i])
            i += 1

    if f_index is not None and f_index + 1 < len(args):
        file_name = args[f_index + 1]

    return directory_path, file_name


def handle_file_creation(directory_path: list, file_name: str) -> None:
    if directory_path:
        dir_path = create_path(directory_path)
        make_directories(dir_path)
        filepath = os.path.join(dir_path, file_name)
    else:
        filepath = file_name

    lines = collect_content_lines()
    write_content_to_file(filepath, lines)


def main() -> None:
    args = sys.argv[1:]
    directory_path, file_name = parse_arguments(args)

    if file_name:
        handle_file_creation(directory_path, file_name)


if __name__ == "__main__":
    main()
