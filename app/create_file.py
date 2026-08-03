import os
from datetime import datetime
import argparse


def parse_arguments() -> tuple[list[str], str | None]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        nargs="+",
        help="Directory path"
    )
    parser.add_argument("-f", "--filename", help="File path")
    args = parser.parse_args()
    directories = args.directory if args.directory else []
    filename = args.filename
    return directories, filename


def create_directories(directories: list[str]) -> str :
    if not directories:
        return ""
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return path


def get_file_content() -> list[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(f"{len(content_lines) + 1} {line}")
    return content_lines


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_exist = os.path.exists(file_path) and os.path.getsize(file_path) > 0
    with open(file_path, "a") as f:
        if file_exist:
            f.write("\n")
        f.write(timestamp + "\n")
        for line in content_lines:
            f.write(line + "\n")


def main() -> None:
    directories, filename = parse_arguments()
    dir_path = create_directories(directories)
    if not filename:
        return

    file_path = os.path.join(dir_path, filename) if dir_path else filename
    lines = get_file_content()
    write_to_file(file_path, lines)


main()
