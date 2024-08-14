import os
import sys

from datetime import datetime


def create_directory(path_parts: str) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created or already exists.")


def create_file(file_path: str) -> None:
    if os.path.exists(file_path):
        append_mode = "a"
    else:
        append_mode = "w"

    with open(file_path, append_mode) as f:
        if append_mode == "a":
            f.write("\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp}\n")

        line_number = sum(
            1 for line in open(file_path)
        ) + 1 if append_mode == "a" else 1

        while True:
            line = input("Enter content line: ")
            if line == "stop":
                f.write("\n")
                break
            f.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("No arguments provided. Use -d for directory and -f for file.")
        return

    path_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            path_parts = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
        else:
            path_parts = args[d_index + 1:]

    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if path_parts:
        create_directory(path_parts)

    if file_name:
        create_file(
            os.path.join(*path_parts)
            if path_parts else ".", file_name
        )


if __name__ == "__main__":
    main()
