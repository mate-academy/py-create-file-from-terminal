import argparse
import os
from datetime import datetime


def create_directory(directory_path: str) -> None:
    dir_path = os.path.join(*directory_path)
    os.makedirs(dir_path, exist_ok=True)


def create_file(file_path: str) -> None:
    content_lines = []
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        content_lines.append(line)

    if not content_lines:
        print("No content provided. File creation aborted.")

    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        content = f"{timestamp}\n"
        content += "\n".join(f"{i+1}. "
                             f"{line}" for i, line in enumerate(content_lines))
        file.write(content)
    print(f"File '{file_path}' created successfully.")


def parse_arguments() -> argparse:
    parser = argparse.ArgumentParser(
        description="Create a directory and file with specified content.")

    parser.add_argument("-d", "--directory", nargs="+", help="Directory path")
    parser.add_argument("-f", "--filename", type=str, help="File name")

    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    if args.directory:
        directory_path = os.path.join(*args.directory)
        create_directory(directory_path)

    if args.filename:
        directory_path = (
            os.getcwd() if not args.directory
            else os.path.join(*args.directory)
        )
        file_path = os.path.join(directory_path, args.filename)
        create_file(file_path)


if __name__ == "__main__":
    main()
