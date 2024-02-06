import os
import argparse
from datetime import datetime


def create_file(filename: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "a") as file:
        file.write(f"{timestamp}\n")
        line = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                break
            file.write(f"Line {line}: {content}\n")
            line += 1


def create_directory(directory_name: str) -> None:
    os.makedirs(directory_name, exist_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="+")
    parser.add_argument("-f", "--file")
    args = parser.parse_args()

    if args.directory:
        folder = os.path.join(*args.directory)
        create_directory(folder)
        print(f"Directory '{folder}' created.")

    if args.file:
        filename = args.file
        if args.directory:
            os.chdir(folder)
        create_file(filename)
        print(f"File '{filename}' created.")


if __name__ == "__main__":
    main()
