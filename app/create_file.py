import sys
import os
from datetime import datetime
from typing import Any


def create_directory(path_parts: Any) -> Any:
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)
    print(f"Directory created: {directory_path}")
    return directory_path


def write_to_file(file_path: Any) -> Any:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    content_lines = []
    line_number = 1
    print("Enter content line (type 'stop' to finish):")

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(f"{line_number} {line}")
        line_number += 1

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n\n")  # Separate previous content
        file.write(f"{timestamp}\n")
        file.write("\n".join(content_lines))
        file.write("\n")

    print(f"Content written to: {file_path}")


def main() -> Any:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [directories] -f [file_name]")
        return

    dir_path = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                dir_path.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
                i += 1
        else:
            print(f"Unknown argument: {args[i]}")
            return

    if not dir_path and not file_name:
        print("You must specify at least -d or -f flag.")
        return

    full_file_path = file_name if file_name else None
    if dir_path:
        directory = create_directory(dir_path)
        if file_name:
            full_file_path = os.path.join(directory, file_name)

    if full_file_path:
        write_to_file(full_file_path)


if __name__ == "__main__":
    main()
