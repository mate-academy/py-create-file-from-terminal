import os

from datetime import datetime
from sys import argv


def create_dir(path: str) -> None:
    """
    Function takes path and recursively creates directories.
    If path is None, - it does nothing
    """
    if not path:
        return
    os.makedirs(path)


def create_empty_file(file_name_with_path: str) -> None:
    if not file_name_with_path:
        return
    if os.path.exists(file_name_with_path):
        return

    with open(file_name_with_path, "w") as file:
        file.write("")


def ask_for_input_and_write_to_file(file_name_with_path: str) -> None:
    """
    Function asks user for input until user enters 'stop'.
    Function writes to a file timestamp and user's input
    """
    with open(file_name_with_path, "a") as file:
        file.write(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
        )

    counter = 1
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        with open(file_name_with_path, "a") as file:
            file.write(f"{counter} {content}\n")
        counter += 1

    with open(file_name_with_path, "a") as file:
        file.write("\n")


def parse_file_name_from_argv() -> str:
    if "-f" not in argv:
        return ""
    return argv[argv.index("-f") + 1]


def parse_directories_from_argv() -> str:
    if "-d" not in argv:
        return ""

    directories = []
    for i in range(argv.index("-d") + 1, len(argv)):
        if argv[i] == "-f":
            break
        directories.append(argv[i])
    return os.path.join(*directories)


def create_from_terminal() -> None:
    directories = parse_directories_from_argv()
    create_dir(directories)

    file_name = parse_file_name_from_argv()
    if not file_name:
        return
    file_name_with_path = os.path.join(directories, file_name)
    create_empty_file(file_name_with_path)

    ask_for_input_and_write_to_file(file_name_with_path)


if __name__ == "__main__":
    create_from_terminal()
