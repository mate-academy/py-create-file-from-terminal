import os
import sys
from datetime import datetime


def create_directory(name_directory: str) -> None:
    parent_dir = os.getcwd()
    path = os.path.join(parent_dir, name_directory)
    try:
        os.makedirs(path)
    except EOFError as error:
        print(f"Error: {error}")


def create_file(file_path: str) -> None:
    file_exist = False
    if os.path.exists(file_path):
        file_exist = True

    with open(file_path, "a") as file:
        date_and_time = datetime.now()
        if file_exist:
            file.write("\n")
        file.write(f"{date_and_time.strftime('%Y-%m-%d %H:%M:%S')}\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        file_index = sys.argv.index("-f") + 1
        directory = os.path.join(*sys.argv[dir_index: file_index - 1])
        filename = sys.argv[file_index]
        create_directory(directory)
        create_file(filename)
    elif "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        directory = os.path.join(*sys.argv[dir_index:])
        create_directory(directory)
    elif "-f" in sys.argv:
        file_index = sys.argv.index("-f") + 1
        filename = sys.argv[file_index]
        create_file(filename)
    else:
        print("Usage:")
        print(
            "python create_file.py"
            " -d <directory_path> - creates directory"
        )
        print(
            "python create_file.py"
            " -f <filename> - creates file and asks for content"
        )
        print(
            "python create_file.py"
            " -d <directory_path>"
            " -f <filename>"
            " - creates directory and file with content")


if __name__ == "__main__":
    main()
