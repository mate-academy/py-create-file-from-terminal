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

    if content_lines:
        with open(file_path, "w") as file:
            file.write("\n".join(content_lines))
        print(f"File '{file_path}' created successfully.")
    else:
        print("No content provided. File creation aborted.")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = f"{timestamp}\n"
    content += "\n".join(f"{i+1}"
                         f"{line}" for i, line in enumerate(content_lines))

    with open(file_path, "a") as file:
        file.write(content)
    print(f"File '{file_path}' created successfully.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create a directory and file with specified content.")

    parser.add_argument("-d", "--directory", nargs="+", help="Directory path")
    parser.add_argument("-f", "--filename", type=str, help="File name")

    args = parser.parse_args()

    if args.directory:
        directory_path = os.path.join(*args.directory)
        create_directory(directory_path)

    if args.filename:
        directory_path = (os.getcwd() if not args.directory
                          else os.path.join(*args.directory))
        file_path = os.path.join(directory_path, args.filename)
        create_file(file_path)
