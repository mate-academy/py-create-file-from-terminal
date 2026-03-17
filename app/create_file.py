import os
import sys
from datetime import datetime


def get_args() -> list[str]:
    return sys.argv[1:]


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    directories = []
    file_name = None
    if "-d" in args:
        d_index = args.index("-d") + 1
        if "-f" in args:
            f_index = args.index("-f")
            directories = args[d_index:f_index]
        else:
            directories = args[d_index:]
    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args):
            file_name = args[f_index]
    return directories, file_name


def create_directories(directories: list[str]) -> str:
    if directories:
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)
        return dir_path
    return "."


def read_content() -> list[str]:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line)
    return lines


def build_content(lines: list[str]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_lines = [
        f"{index} {line}" for index, line in enumerate(lines, start=1)
    ]
    return f"{timestamp}\n" + "\n".join(numbered_lines)


def write_to_file(file_path: str, content: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(content)
        file.write("\n")


def main() -> None:
    args = get_args()
    directories, file_name = parse_args(args)
    if not directories and file_name is None:
        print("Use -d for directories and/or -f for file name.")
        return
    dir_path = create_directories(directories)
    if file_name is not None:
        file_path = os.path.join(dir_path, file_name)
        lines = read_content()
        content = build_content(lines)
        write_to_file(file_path, content)


if __name__ == "__main__":
    main()
