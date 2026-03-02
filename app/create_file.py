import sys
import os
from datetime import datetime
from typing import List, Tuple, Optional


def get_arguments() -> Tuple[List[str], Optional[str]]:
    args: List[str] = sys.argv[1:]

    directories: List[str] = []
    filename: Optional[str] = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            directories = args[d_index + 1:f_index]
        else:
            directories = args[d_index + 1:]

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]
        else:
            print("Error: No filename provided after -f flag.")
            sys.exit(1)

    return directories, filename


def create_directories(directories: List[str]) -> str:
    if directories:
        path: str = os.path.join(*directories)
        os.makedirs(path, exist_ok=True)
        return path
    return ""


def get_content_from_user() -> List[str]:
    lines: List[str] = []
    counter: int = 1

    while True:
        line: str = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(f"{counter} {line}")
        counter += 1

    return lines


def write_to_file(
    path: str,
    filename: str,
    content_lines: List[str],
) -> None:
    full_path: str = os.path.join(path, filename) if path else filename

    timestamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists: bool = os.path.exists(full_path)

    with open(full_path, "a", encoding="utf-8") as file:
        if file_exists:
            file.write("\n")

        file.write(f"{timestamp}\n")
        for line in content_lines:
            file.write(f"{line}\n")

    print(f"File created/updated at: {full_path}")


def main() -> None:
    directories, filename = get_arguments()

    if directories and not filename:
        create_directories(directories)
        print("Directories created successfully.")
        return

    if filename:
        path: str = create_directories(directories)
        content_lines: List[str] = get_content_from_user()
        write_to_file(path, filename, content_lines)
    else:
        print("Error: You must provide at least -d or -f flag.")
