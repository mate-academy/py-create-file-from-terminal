import os
import sys
from datetime import datetime


def create_directory(path_parts: list) -> str:
    """
    Creates a directory path by joining the list of path parts.
    If the directory does not exist, it will be created.

    :param path_parts: List of directory names that form the full path.
    :return: The full directory path as a string.
    """
    full_path = os.path.join(*path_parts)
    os.makedirs(full_path, exist_ok=True)
    return str(full_path)


def write_file(file_path: str) -> None:
    """
    Opens the file at the given path and writes user input to it.
    Adds a timestamp and line numbers to the content.
    If the file already exists, appends new content.

    Prompts the user for input until the "stop" command is entered.

    :param file_path: The path of the file to write or append content to.
    :return: None
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "a") as file:
        file.write(f"{timestamp}\n")
        line_number = 1

        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    """
    The main function that handles command-line arguments to create directories
    and/or files based on the flags entered.

    - If -d flag is used, it creates directories from the entered path parts.
    - If -f flag is used, it creates or appends to a file, allowing the user
      to input content line by line, until the "stop" command is entered.
    - If both flags are used, the file creates inside the specified directory.

    :return: None
    """
    args = sys.argv[1:]

    if not args:
        print("No argument entered. Use -d for directories or -f for files.")
        return

    directory_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d") + 1
        while d_index < len(args) and not args[d_index].startswith("-"):
            directory_parts.append(args[d_index])
            d_index += 1

    if "-f" in args:
        f_index = args.index("-f") + 1
        if f_index < len(args) and not args[f_index].startswith("-"):
            file_name = args[f_index]

    if not directory_parts and not file_name:
        print("Please enter valid -d or -f arguments.")
        return

    if directory_parts:
        dir_path = create_directory(directory_parts)
        print(f"Directory created: {dir_path}")
    else:
        dir_path = os.getcwd()

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        print(f"Creating file: {file_path}")
        write_file(file_path)


if __name__ == "__main__":
    main()
