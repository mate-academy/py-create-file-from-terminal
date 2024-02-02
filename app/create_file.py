import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def read_lines() -> list:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        lines.append(line)
    return lines


def create_file(file_path: str, lines: list) -> None:
    with open(file_path, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")


def get_flag_index(flag: str) -> int | None:
    return sys.argv.index(flag) if flag in sys.argv else None


def get_flag_value(flag: str) -> str | None:
    index = get_flag_index(flag)
    return sys.argv[index + 1] if index is not None else None


def get_dir_path() -> str:
    dir_index = get_flag_index("-d")
    file_index = get_flag_index("-f")

    if dir_index is not None:
        end_index = (
            file_index if file_index is not None and file_index > dir_index
            else len(sys.argv)
        )
        return os.path.join(*sys.argv[dir_index + 1:end_index])


def parse_args() -> tuple:
    dir_path = get_dir_path() if get_flag_index("-d") is not None else ""
    file_name = get_flag_value("-f")
    return dir_path, file_name


def main() -> None:
    dir_path, file_name = parse_args()

    if dir_path:
        create_directory(dir_path)

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        lines = read_lines()
        create_file(file_path, lines)


if __name__ == "__main__":
    main()
