import sys
import os
from datetime import datetime


def create_directory(path_parts: str) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_or_append_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"File already exists, appending to it: {file_path}")
    else:
        print(f"Creating new file: {file_path}")

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_count = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_count} {line}\n")
            line_count += 1


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        dir_index = args.index("-d")
        dir_path = args[dir_index + 1:]
        create_directory(dir_path)

    if "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]

        if "-d" in args:
            dir_path = args[args.index("-d") + 1:file_index]
            file_path = os.path.join(*dir_path, file_name)
        else:
            file_path = file_name

        create_or_append_file(file_path)


if __name__ == "__main__":
    main()
