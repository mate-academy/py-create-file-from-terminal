import sys
import os
from datetime import datetime


def create_directory(args: list) -> str | bytes:
    path = os.path.join(*args)
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_name: str, path: str = ".", mode: str = "w") -> None:
    file_path = os.path.join(path, file_name)
    if os.path.exists(file_path):
        mode = "a"
    with open(file_path, mode) as file:
        if mode == "a":
            file.write("\n")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"\n{timestamp}")

        number_of_line = 1
        while True:
            content_line = input(f"Enter content line: ")
            if content_line.lower() == "stop":
                break
            file.write(f"\n{number_of_line} {content_line}")
            number_of_line += 1


def main() -> None:
    command = sys.argv
    if "-f" in command and "-d" in command:
        path = create_directory(command[2:-2])
        create_file(command[-1], path)
    elif "-d" in command:
        create_directory(command[2:])
    elif "-f" in command:
        create_file(command[-1])


if __name__ == "__main__":
    main()
