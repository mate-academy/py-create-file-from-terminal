import os
import sys
from datetime import datetime


def create_dir(path: str) -> None:
    path = os.path.join(*path)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        directory_parts = []
        for arg in args[d_index + 1:]:
            directory_parts.append(arg)
        directory_path = create_dir(directory_parts)
    else:
        directory_path = "."

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)


if __name__ == "__main__":
    main()
