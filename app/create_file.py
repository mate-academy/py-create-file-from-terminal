import os
import argparse
from datetime import datetime


def create_directory(way: str) -> None:
    os.makedirs(way, exist_ok=True)
    current_directory = os.getcwd()
    os.chdir(os.path.join(current_directory, way))


def create_file(name: str) -> None:
    count_lines = 1
    file_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            break
        file_content += f"\n{count_lines} {line}"
        count_lines += 1
    with open(name, "a") as file:
        if os.stat(name).st_size > 0:
            file.write("\n")
        file.write(file_content)


def main() -> None:

    parser = argparse.ArgumentParser()

    parser.add_argument("-d", dest="directory", nargs="*")
    parser.add_argument("-f", dest="file")
    args = parser.parse_args()

    if args.directory:
        create_directory(os.path.join(*list(args.directory)))
    if args.file:
        create_file(args.file)


if __name__ == "__main__":
    main()
