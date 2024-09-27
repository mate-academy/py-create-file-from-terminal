from typing import Any
import sys
import os
from datetime import datetime


def create_directories(path_parts: Any) -> None:
    path = os.path.join(*path_parts)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def get_timestamp() -> None:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_content() -> None:
    lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)
    return lines


def write_to_file(filepath: Any, content_lines: Any) -> None:
    timestamp = get_timestamp()

    if os.path.exists(filepath):
        append_write = "a"
    else:
        append_write = "w"

    with open(filepath, append_write) as f:
        if append_write == "a":
            f.write("\n\n")
        f.write(f"{timestamp}\n")

        for i, line in enumerate(content_lines, start=1):
            f.write(f"{i} {line}\n")

    print(f"Content successfully written to {filepath}")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        dir_index = args.index("-d") + 1
        if "-f" in args:
            file_index = args.index("-f") + 1
            directory_parts = args[dir_index:file_index - 1]
            directory_path = create_directories(directory_parts)
            file_name = args[file_index]
            filepath = os.path.join(directory_path, file_name)
        else:
            directory_parts = args[dir_index:]
            create_directories(directory_parts)
            print(f'Directory {"/".join(directory_parts)} created.')
            return
    elif "-f" in args:
        # Only file provided
        file_index = args.index("-f") + 1
        file_name = args[file_index]
        filepath = os.path.join(os.getcwd(), file_name)
    else:
        print("Usage: python create_file.py [-d directory] [-f filename]")
        return

    content_lines = get_content()
    write_to_file(filepath, content_lines)


if __name__ == "__main__":
    main()
