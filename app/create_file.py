import os
import sys
import argparse
from datetime import datetime


def create_directory(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)


def create_file(file_name: str, content: list[str]) -> None:
    with open(file_name, "a") as file:
        file.write("\n\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(timestamp + "\n")
        for index, line in enumerate(content, start=1):
            file.write(f"{index} {line}\n")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create directory or file with content"
    )
    parser.add_argument("-d",
                        "--directory",
                        nargs="+",
                        help="Directory path to create")
    parser.add_argument("-f",
                        "--filename",
                        help="File name to create")
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()
    if not args.directory and not args.filename:
        print("Please provide flags (-d or -f)")
        sys.exit(1)

    if args.directory:
        directory = os.path.join(*args.directory)
        filename = args.filename if args.filename else "file.txt"
    else:
        directory = None
        filename = args.filename

    content = []
    print("Enter content (use 'stop' to finish editing):")
    while True:
        line = input()
        if line.lower() == "stop":
            break
        content.append(line)

    if directory:
        create_directory(directory)
        if filename:
            file_path = os.path.join(directory, filename)
            create_file(file_path, content)
    elif filename:
        create_file(filename, content)


if __name__ == "__main__":
    main()
