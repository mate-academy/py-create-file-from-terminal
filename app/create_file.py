import os
import argparse
from datetime import datetime


def create_file(file_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    numbered_content = "\n".join([f"{i} {line}" for i, line
                                  in enumerate(content_lines, start=1)])
    file_content = f"{timestamp}\n{numbered_content}\n"

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n\n" + file_content)
    else:
        with open(file_path, "w") as file:
            file.write(file_content)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directory and/or file with content.")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-d", "--directory", nargs="+", help="Create directory")
    group.add_argument("-f", "--file", help="Create file")
    args = parser.parse_args()

    if args.directory:
        dir_path = os.path.join(*args.directory)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    elif args.file:
        file_path = args.file
        content_lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            content_lines.append(line)
        create_file(file_path, content_lines)


if __name__ == "__main__":
    main()
