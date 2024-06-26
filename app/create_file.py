import sys
import os
from datetime import datetime
from typing import List


def create_directory(path_parts: List[str]) -> str:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created successfully.")
    return path


def create_file(file_path: str) -> None:
    lines = []
    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(file_path):
        mode = "a"
    else:
        mode = "w"

    with open(file_path, mode) as f:
        f.write(f"{timestamp}\n")
        for i, line in enumerate(lines, start=1):
            f.write(f"{i} {line}\n")
        f.write("\n")

    print(f"File '{file_path}' created/updated successfully.")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        dir_index = args.index("-d")
        if "-f" in args:
            file_index = args.index("-f")
            dir_parts = args[dir_index + 1:file_index]
            file_name = args[file_index + 1]
            if not dir_parts or not file_name:
                print("Error: Invalid directory or file name.")
                return
            dir_path = create_directory(dir_parts)
            file_path = os.path.join(dir_path, file_name)
        else:
            dir_parts = args[dir_index + 1:]
            if not dir_parts:
                print("Error: Invalid directory path.")
                return
            create_directory(dir_parts)
            return

    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        if not file_name:
            print("Error: Invalid file name.")
            return
        file_path = os.path.join(os.getcwd(), file_name)
    else:
        print("Error: No valid flags provided.")
        return

    create_file(file_path)


if __name__ == "__main__":
    main()
