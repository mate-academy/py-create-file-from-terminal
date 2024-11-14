import sys
import os
from datetime import datetime


def create_directory(path_parts: list) -> None:
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_file(file_path: str) -> None:
    mode = "a" if os.path.exists(file_path) else "w"

    with open(file_path, mode) as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1

    print(f"File created/updated: {file_path}")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        path_parts = args[args.index("-d") + 1:args.index("-f")] \
            if "-f" in args \
            else args[args.index("-d") + 1:]
        create_directory(path_parts)

    if "-f" in args:
        file_name = args[args.index("-f") + 1]
        file_path = os.path.join(*path_parts, file_name) \
            if "-d" in args \
            else file_name
        create_file(file_path)


if __name__ == "__main__":
    main()
