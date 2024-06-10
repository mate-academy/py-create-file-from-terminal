import os
import sys
from datetime import datetime


def make_directories(args: list) -> str | bytes:
    dir_path = os.path.join(*args)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def create_file(filename: str, path: str = ".") -> None:
    file_path = os.path.join(path, filename)
    with open(file_path, "a") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 0
        while True:
            line_number += 1
            file_input = input("Enter content line: ")
            if file_input == "stop":
                file.write("\n")
                break
            file.write(f" {line_number} {file_input} \n")


def main() -> None:
    command = sys.argv
    if "-d" in command and "-f" in command:
        path = make_directories(command[2:-2])
        create_file(command[-1], path)
    elif "-d" in command:
        make_directories(command[2:])
    elif "-f" in command:
        create_file(command[-1])


if __name__ == "__main__":
    main()
