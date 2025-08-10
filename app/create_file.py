import sys
import os
from datetime import datetime


def create_directory(path_parts: str) -> str:
    """Create directories specified in path_parts."""
    directory_path = os.path.join(*path_parts)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' created.")
    else:
        print(f"Directory '{directory_path}' already exists.")
    return directory_path


def create_file(file_path: str) -> None:
    """Create a file and append user input content with a timestamp."""
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1
        print(f"Content written to '{file_path}'.")


def main() -> None:
    args = sys.argv[1:]

    if not args:
        print("No arguments provided. "
              "Please use -d for directory and/or -f for file.")
        return

    directory_parts = []
    file_name = None
    i = 0

    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] != "-f":
                directory_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                file_name = args[i]
            else:
                print("No file name provided after -f flag.")
                return
            i += 1
        else:
            i += 1

    if directory_parts:
        directory_path = create_directory(directory_parts)
    else:
        directory_path = os.getcwd()

    if file_name:
        file_path = os.path.join(directory_path, file_name)
        create_file(file_path)
    else:
        if not directory_parts:
            print("No operation specified. "
                  "Please provide a directory with -d or a file with -f.")
        else:
            print("Directory created without a file.")


if __name__ == "__main__":
    main()
