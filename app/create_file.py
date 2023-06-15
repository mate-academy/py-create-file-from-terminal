import sys
from datetime import datetime
import os


def create_file(file_path: str) -> None:
    line_number = 1
    with open(file_path, "a") as file:
        file.write(f"{datetime.now().strftime('%A, %I:%M%p')} \n")
        while True:
            text = input("Enter content line: ")
            if text == "stop":
                break
            file.write(f"{line_number} {text}\n")
            line_number += 1
        file.write("\n")


def create_file_through_terminal() -> None:
    if "-f" not in sys.argv and "-d" in sys.argv:
        dir_path = ""
        for directory in sys.argv[2:]:
            dir_path = os.path.join(dir_path, directory)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in sys.argv and "-d" not in sys.argv:
        file_name = sys.argv[-1]
        create_file(file_name)

    if "-f" in sys.argv and "-d" in sys.argv:
        path_parts = sys.argv[2:]
        path_parts.remove("-f")
        path = ""

        for directory in path_parts:
            path = os.path.join(path, directory)

        dir_path = os.path.dirname(path)
        os.makedirs(dir_path, exist_ok=True)
        create_file(path)


if __name__ == "__main__":
    create_file_through_terminal()
