import os
import argparse
from datetime import datetime


def create_file(directory: str, filename: str, content: list[str]) -> None:
    if directory:
        os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    mode = "w" if not os.path.exists(filepath) else "a"
    with open(filepath, mode) as file:
        if mode == "a":
            file.write("\n\n")
        file.write(timestamp + "\n")
        for index, line in enumerate(content, start=1):
            file.write(f"{index} {line}\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create directory or file with content")
    parser.add_argument(
        "-d", "--directory", nargs="+", help="Directory path to create")
    parser.add_argument("-f", "--filename", help="File name to create")
    args = parser.parse_args()

    if not args.directory and not args.filename:
        parser.error("Please provide either -d or -f flag.")

    if args.directory:
        directory = os.path.join(*args.directory)
        filename = args.filename if args.filename else "file.txt"
    else:
        directory = None
        filename = args.filename

    content = []
    print("Enter content lines (type 'stop' to finish):")
    while True:
        line = input()
        if line.lower() == "stop":
            break
        content.append(line)

    create_file(directory, filename, content)
    print("Directory/File created successfully.")


if __name__ == "__main__":
    main()
