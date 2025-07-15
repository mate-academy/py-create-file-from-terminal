import sys
import os
from datetime import datetime
from typing import List, Optional, Tuple


def parse_arguments(arguments: List[str]) -> Tuple[List[str], Optional[str]]:
    directory_parts: List[str] = []
    filename: Optional[str] = None
    current_flag: Optional[str] = None
    for arg in arguments:
        if arg == "-d":
            current_flag = "-d"
            continue
        if arg == "-f":
            current_flag = "-f"
            continue
        if current_flag == "-d":
            directory_parts.append(arg)
        elif current_flag == "-f":
            if filename is not None:
                print("Error: Only one filename is allowed after -f flag.")
                sys.exit(1)
            filename = arg
        else:
            print(f"Error: Unexpected argument '{arg}'. Use -d and -f flags properly.")
            sys.exit(1)
    return directory_parts, filename


def create_directory_path(parts: List[str]) -> Optional[str]:
    if not parts:
        return None
    path = os.path.join(*parts)
    os.makedirs(path, exist_ok=True)
    return path


def read_content_lines() -> List[str]:
    print("Enter content line:", end=" ")
    content_lines: List[str] = []
    while True:
        line = input()
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)
        print("Enter content line:", end=" ")
    return content_lines


def append_content_to_file(filepath: str, lines: List[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    lines_to_write = [f"{timestamp}\n"] + [
        f"{index} {content}\n"
        for index, content in enumerate(lines, start=1)
    ]
    mode = "a" if os.path.exists(filepath) else "w"
    with open(filepath, mode, encoding="utf-8") as file:
        if mode == "a":
            file.write("\n")
        file.writelines(lines_to_write)


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print(
            "Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]"
        )
        sys.exit(1)

    directories, filename = parse_arguments(args)

    if directories and not filename:
        created_path = create_directory_path(directories)
        print(f"Directory created: {created_path}")
        return

    if filename:
        target_dir = create_directory_path(directories) if directories else ""
        filepath = os.path.join(target_dir, filename) if target_dir else filename
        content_lines = read_content_lines()
        append_content_to_file(filepath, content_lines)
        print(f"File '{filepath}' created/updated successfully.")
    else:
        print("Error: Filename (-f) must be specified to create a file.")
        sys.exit(1)


if __name__ == "__main__":
    main()
