import os
from datetime import datetime
import argparse


def get_file_content() -> list:
    content = []
    while True:
        print("Enter 'stop' if you want to quit")
        message = input("Enter content line: ")
        if message == "stop":
            break
        content.append(message)

    return content


def create_file(file_name: str, content: list) -> None:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_name, "a") as file:
        file.write(f"{current_time}\n")
        for line_number, line in enumerate(content, start=1):
            file.write(f"{line_number} {line}\n")
        file.write("\n")


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)


def create_directory_and_file(directory: str,
                              file_name: str,
                              content: list) -> None:
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, file_name)
    create_file(path, content)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create"
                                                 "files and directories "
                                                 "with content"
                                                 "and timestamps.")
    parser.add_argument("-d",
                        dest="directory",
                        nargs="+",
                        help="Create a directory with the given path.")
    parser.add_argument("-f",
                        dest="file",
                        help="Create a file with the given name and content.")

    args = parser.parse_args()

    if args.directory and args.file:
        path = os.path.join(*args.directory)
        create_directory_and_file(path, args.file, get_file_content())
    elif args.file:
        create_file(args.file, get_file_content())
    elif args.directory:
        path = os.path.join(*args.directory)
        create_directory(path)


if __name__ == "__main__":
    main()
