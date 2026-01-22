import os
import sys
from datetime import datetime


def create_directory(path_parts: str) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")
    return path


def create_or_append_file(file_path: str) -> None:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")
        file.write(f"{timestamp}\n")
        for i, line in enumerate(content_lines, 1):
            file.write(f"{i} {line}\n")

    print(f"File written: {file_path}")


def main() -> None:
    args = sys.argv[1:]

    if not args or ("-d" not in args and "-f" not in args):
        sys.exit(1)

    dir_path = []
    file_name = None
    current_flag = None

    for arg in args:
        if arg == "-d":
            current_flag = "-d"
        elif arg == "-f":
            current_flag = "-f"
        elif current_flag == "-d":
            dir_path.append(arg)
        elif current_flag == "-f":
            file_name = arg

    if dir_path:
        directory = create_directory(dir_path)
    else:
        directory = os.getcwd()

    if file_name:
        file_path = os.path.join(directory, file_name)
        create_or_append_file(file_path)
    else:
        print("No file name provided.")


if __name__ == "__main__":
    main()
