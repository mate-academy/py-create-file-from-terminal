from datetime import datetime
from typing import Tuple
import os
import sys


def parse_arguments(argv: list) -> Tuple[str, str]:
    new_directory = ""
    new_file_name = "file.txt"

    if "-f" in argv:
        index = argv.index("-f")
        new_file_name = argv[index + 1]
        argv.remove(argv[index])
        argv.remove(argv[index])

    if "-d" in argv:
        index = argv.index("-d")
        directory_parts = argv[index + 1:]
        for path in directory_parts:
            new_directory = os.path.join(new_directory, path)

        os.makedirs(new_directory, exist_ok=True)

    file_path = os.path.join(new_directory, new_file_name)
    return new_directory, file_path


def write_user_input(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_number = 1
        while True:
            content = input("Enter content line: ")

            if content.lower() == "stop":
                break

            file.write(f"{line_number} {content}\n")
            line_number += 1

        file.write("\n")


def main() -> None:
    _, file_path = parse_arguments(sys.argv)
    write_user_input(file_path)


if __name__ == "__main__":
    main()
