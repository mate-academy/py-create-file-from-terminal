import argparse
import os
import sys
from datetime import datetime

def create_path(directories) -> str:
    path = os.path.join(*directories)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def create_file(path: str) -> None:
    with open(path, "w") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_count = 0
        content = ""
        while content != "stop":
            content = input("Enter content line: ")
            line_count += 1
            file.write(f"{line_count}. {content}\n")

def main():
    terminal_input = argparse.ArgumentParser()
    terminal_input.add_argument('-d', '--directories', nargs='+')
    terminal_input.add_argument('-f', '--file_name')
    args = terminal_input.parse_args()
    directories, file_name = args.directories, args.file_name
    if not file_name and not directories:
        print("Please, provide a valid command: "
              "'-d <directory_1> <directory_2>' or '-f <file_name>'"
        )
        sys.exit(1)
    path = ""
    if directories:
        path = create_path(directories)

    if file_name:
        path = os.path.join(path, file_name)
        create_file(path)
    sys.exit(1)


if __name__ == "__main__":
    main()