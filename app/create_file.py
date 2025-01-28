import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_file(file_name: str) -> None:
    content_lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_content = [f"{i+1} {line}" for i, line in enumerate(content_lines)]

    with open(file_name, "a") as file:
        file.write(f"\n{timestamp}\n")
        file.write("\n".join(numbered_content))
        file.write("\n")


def main() -> None:
    args = sys.argv[1:]

    if "-d" in args:
        d_index = args.index("-d")
        dir_path = os.path.join(*args[d_index + 1:])
        create_directory(dir_path)

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        if "-d" in args:
            dir_path = os.path.join(*args[args.index("-d") + 1: f_index])
            file_name = os.path.join(dir_path, file_name)
        create_file(file_name)


if __name__ == "__main__":
    main()
