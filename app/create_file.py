import sys
import os
import datetime
from typing import List, Optional


def create_file_with_content(
        file_path: str, content_lines: List[str]
) -> None:
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"{timestamp}\n")
        for index, line in enumerate(content_lines, start=1):
            file.write(f"{index} {line}\n")
        file.write("\n")


def create_directories(dir_path: List[str]) -> None:
    full_path = os.path.join(*dir_path)
    os.makedirs(full_path, exist_ok=True)


def get_content_from_terminal() -> List[str]:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)
    return content_lines


def main() -> None:
    args = sys.argv[1:]
    dir_path: List[str] = []
    file_name: Optional[str] = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_path = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
        else:
            dir_path = args[d_index + 1:]
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if dir_path:
        create_directories(dir_path)

    if file_name:
        if dir_path:
            file_path = os.path.join(*dir_path, file_name)
        else:
            file_path = file_name
        content_lines = get_content_from_terminal()
        create_file_with_content(file_path, content_lines)


if __name__ == "__main__":
    main()
