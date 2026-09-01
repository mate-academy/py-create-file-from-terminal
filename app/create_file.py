import os
import sys
from datetime import datetime


def create_directory(directory_path: str) -> None:
    os.makedirs(directory_path, exist_ok=True)


def get_file_content() -> list[str]:
    content = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n"
    content.append(timestamp)
    count = 1
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content.append(f"{count} {line}\n")
        count += 1
    return content


def write_to_file(file_path: str, file_content: list[str]) -> None:
    with open(file_path, "a") as file:
        if os.path.getsize(file_path) != 0:
            file.write("\n")
        file.writelines(file_content)


def parse_args(args: list[str]) -> tuple[list[str], str | None]:
    dir_parts = []
    file_name = None
    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            i += 1
    return dir_parts, file_name


args = sys.argv[1:]
dir_parts, file_name = parse_args(args)

dir_path = os.path.join(*dir_parts) if dir_parts else ""

if dir_path:
    create_directory(dir_path)

if file_name:
    file_path = os.path.join(dir_path, file_name) if dir_path else file_name
    write_to_file(file_path, get_file_content())
