import sys
import os
from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_directories(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def write_to_file(file_path: str) -> None:
    print("Enter content line (type 'stop' to finish):")
    content_lines = []

    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    if content_lines:
        with open(file_path, "a") as file:
            file.write(f"\n{get_timestamp()}\n")
            for i, line in enumerate(content_lines, 1):
                file.write(f"{i} {line}\n")


def main():
    args = sys.argv[1:]
    if not args:
        print("Set arguments")
        return

    dir_path, file_name = "", ""

    if "-d" in args:
        d_index = args.index("-d")
        f_index = args.index("-f") if "-f" in args else None
        dir_path = str(os.path.join(*args[d_index + 1: f_index or None]))

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1] if f_index + 1 < len(args) else None

    if dir_path:
        create_directories(dir_path)

    if file_name:
        file_path = os.path.join(dir_path, file_name) if dir_path else file_name
        write_to_file(file_path)
    else:
        create_directories(dir_path)


if __name__ == "__main__":
    main()

