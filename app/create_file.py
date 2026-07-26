import sys
import os
from datetime import datetime


def create_directory(path_parts: list) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        print(f"File {file_path} already exists. Appending content.")
    else:
        print(f"Creating file: {file_path}")

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
    path_parts = []
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d")
        for arg in sys.argv[dir_index + 1:]:
            if arg.startswith("-"):
                break
            path_parts.append(arg)
        if not path_parts:
            print("Error: No directory specified after -d flag.")
            return
        create_directory(path_parts)

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f")
        file_name = None
        for arg in sys.argv[file_index + 1:]:
            if arg.startswith("-"):
                break
            file_name = arg
            break
        if not file_name:
            print("Error: No file name specified after -f flag.")
            return
        dir_path = os.path.join(*path_parts) if path_parts else "."
        file_path = os.path.join(dir_path, file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
