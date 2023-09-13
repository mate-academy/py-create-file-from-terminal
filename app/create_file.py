from __future__ import annotations

import sys

import os

import datetime


def create_file(file_path: str, content_lines: list[str]) -> None:
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(current_time + "\n")
        for i, line in enumerate(content_lines, start=1):
            file.write(f"{i} {line}\n")


def get_file_path() -> str | None:
    if len(sys.argv) < 3:
        print("Usage: python create_file.py -d directory_path OR -f file_name")
        return None

    if sys.argv[1] == "-d":
        directory_path = os.path.join(*sys.argv[2:])
        os.makedirs(directory_path, exist_ok=True)
        file_name = input("Enter the file name: ")
        file_path = os.path.join(directory_path, file_name)
    elif sys.argv[1] == "-f":
        file_path = sys.argv[2]
    else:
        print("Invalid option. Use -d for directory or -f for file.")
        return None

    return file_path


def main() -> None:
    file_path = get_file_path()

    if not file_path:
        return

    content_lines = []
    while True:
        line = input("Enter content line (or 'stop' to finish): ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    create_file(file_path, content_lines)
    print(f"File '{file_path}' created successfully.")


if __name__ == "__main__":
    main()
