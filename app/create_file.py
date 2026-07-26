from datetime import datetime
from os import makedirs
from pathlib import Path
from sys import argv

from parsing import parse_path


def create_file_from_terminal() -> None:
    """
    run in the terminal from the app package
    this way -> "python -m create_file ..."
    """
    directories, file_name = parse_path(argv)
    makedirs(Path(*directories), exist_ok=True)
    full_path = Path(*directories, file_name)

    if file_name:
        content = ""

        try:
            with open(full_path) as file_to_check:
                if file_to_check.read():
                    content += "\n\n"

        except FileNotFoundError:
            pass

        content += f"{datetime.now()}\n"
        counter = 1

        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                break
            content += f"{counter} {content_line}\n"
            counter += 1

        with open(Path(*directories, file_name), "a") as file_to_write:
            file_to_write.write(content.rstrip())


if __name__ == "__main__":
    create_file_from_terminal()
