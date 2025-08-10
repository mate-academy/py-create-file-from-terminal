import sys
import os
from datetime import datetime


def create_directory(path_parts: str) -> str:
    path = os.path.join(*path_parts)
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")

        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    command = sys.argv
    if "-d" in command and "-f" in command:
        d_index = command.index("-d")
        f_index = command.index("-f")
        dir_parts = command[d_index + 1:f_index]
        file_name = command[f_index + 1]

        if not dir_parts or not file_name:
            print("Error: Invalid arguments.")
            return

        dir_path = create_directory(dir_parts)
        file_path = os.path.join(dir_path, file_name)
        create_file(file_path)

    elif "-d" in command:
        dir_parts = command[command.index("-d") + 1:]
        if not dir_parts:
            print("Error: No directory specified after -d")
            return

        create_directory(dir_parts)

    elif "-f" in command:
        file_index = command.index("-f") + 1
        if file_index >= len(command):
            print("Error: No file name specified after -f")
            return

        file_name = command[file_index]
        create_file(file_name)


if __name__ == "__main__":
    main()
