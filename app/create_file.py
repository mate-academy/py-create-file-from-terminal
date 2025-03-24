import sys
import os
import argparse
from datetime import datetime


def create_directory(path: any) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory '{path}' created (or already exists).")


def write_to_file(file_path: any) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_lines = []
    line_number = 1
    print("Enter file content (type 'stop' to finish):")
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content_lines.append(f"{line_number} {line}")
        line_number += 1

    with open(file_path, "a", encoding="utf-8") as file:
        if os.path.getsize(file_path) > 0:
            file.write("\n\n")
        file.write(f"{timestamp}\n")
        file.write("\n".join(content_lines) + "\n")
    print(f"File '{file_path}' updated.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Create directories "
                                                 "and files with content.")
    parser.add_argument("-d", "--directory", nargs="*",
                        help="Specify the directory path.")
    parser.add_argument("-f", "--file", help="Specify the file name.")

    args = parser.parse_args()

    if args.directory:
        full_dir_path = os.path.join(os.getcwd(), *args.directory)
        create_directory(full_dir_path)
    else:
        full_dir_path = os.getcwd()

    if args.file:
        file_path = os.path.join(full_dir_path, args.file)
        write_to_file(file_path)
    else:
        print("No file specified. Exiting.")
        sys.exit(1)


if __name__ == "__main__":
    main()
