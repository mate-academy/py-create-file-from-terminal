import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    try:
        os.makedirs(path)
    except FileExistsError:
        print(f"Directory already exists at path: {path}")
    else:
        print(f"Directory created at path: {path}")


def create_file(name: str, path: str = "") -> None:
    filepath = os.path.join(path, name)
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        lines.append(line + "\n")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if lines:
        formatted_content = [f"{i + 1} {line}" for i, line in enumerate(lines)]
        content_to_write = f"{timestamp}\n" + "".join(formatted_content)
    else:
        content_to_write = f"{timestamp}\n"

    if os.path.exists(filepath):
        with open(filepath, "a") as file:
            file.write(content_to_write)
        print(f"Appended content to existing file: {filepath}")
    else:
        with open(filepath, "w") as file:
            file.write(content_to_write)
        print(f"Created file: {filepath}")


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = ""

    if "-d" in args:
        dir_command_index = args.index("-d")
        if "-f" in args:
            file_command_index = args.index("-f")
            path_parts = args[dir_command_index + 1:file_command_index]
            filename = args[file_command_index + 1]
        else:
            path_parts = args[dir_command_index + 1:]

        dir_path = os.path.join(*path_parts)
        create_directory(dir_path)
        if filename:
            create_file(path=dir_path, name=filename)

    elif "-f" in args:
        file_command_index = args.index("-f")
        create_file(name=args[file_command_index + 1])
    else:
        print("Invalid arguments. Use -d to specify directories and -f to specify filename.")
