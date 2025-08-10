import os
import argparse
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    file_path = os.path.join(directory, filename)

    with open(file_path, "a+") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in content_input():
            file.write(line + "\n")


def create_dir(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)


def content_input() -> None:
    print("Enter content line (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        yield line + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create file with content")
    parser.add_argument("-d",
                        "--directory",
                        help="Directory path",
                        nargs="+",
                        default="")
    parser.add_argument("-f", "--filename", help="File name", default="")
    args = parser.parse_args()

    dir_paths = args.directory
    filename = args.filename

    dir_path = os.path.join(*dir_paths)

    if dir_path:
        create_dir(dir_path)
    if filename:
        create_file(dir_path, filename)


if __name__ == "__main__":
    main()
