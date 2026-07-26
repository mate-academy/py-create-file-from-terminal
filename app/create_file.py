import os
import sys
from datetime import datetime


def get_content() -> list:
    content_lines = []
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)
    return content_lines


def write_to_file(file_path: str, content: list) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as target_file:
        target_file.write(f"{timestamp}\n")
        for index, line in enumerate(content, start=1):
            target_file.write(f"{index} {line}\n")
        target_file.write("\n")


def main() -> None:
    args = sys.argv
    directories = []
    filename = ""

    if "-d" in args:
        d_index = args.index("-d")
        for i in range(d_index + 1, len(args)):
            if args[i].startswith("-"):
                break
            directories.append(args[i])

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            filename = args[f_index + 1]

    current_path = os.getcwd()
    if directories:
        current_path = os.path.join(current_path, *directories)
        os.makedirs(current_path, exist_ok=True)

    if filename:
        file_path = os.path.join(current_path, filename)
        content = get_content()
        write_to_file(file_path, content)


if __name__ == "__main__":
    main()
