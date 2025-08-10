import os
import sys
from datetime import datetime

arguments = sys.argv


def create_directory(directory_path: list) -> None:
    os.makedirs(os.path.join(*directory_path), exist_ok=True)
    os.chdir(os.path.join(*directory_path))


def create_file(file_name: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_count = 1

    with open(file_name, "a" if os.path.exists(file_name) else "w") as file:
        if file.tell() != 0:
            file.write("\n\n")
        file.write(timestamp)
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"\n{line_count} {line}")
            line_count += 1


def command_check() -> None:
    if len(arguments) < 2:
        print(
            "Usage: python create_file.py -d <directory_path> -f <file_name>"
        )
        sys.exit(1)


def flags_check() -> None:
    if "-d" in arguments and "-f" in arguments:
        index_d = arguments.index("-d")
        index_f = arguments.index("-f")
        file_to_create = arguments[index_f + 1]
        if index_d < index_f:
            directory_path = arguments[index_d + 1:index_f]
            create_directory(directory_path)
            create_file(file_to_create)
        else:
            directory_path = arguments[index_d + 1:]
            create_directory(directory_path)
            create_file(file_to_create)
    elif "-d" in arguments and "-f" not in arguments:
        directory_path = arguments[2:]
        create_directory(directory_path)
    elif "-d" not in arguments and "-f" in arguments:
        file_to_create = arguments[2]
        create_file(file_to_create)
    elif "-d" not in arguments and "-f" not in arguments:
        print("Invalid flag. Use -d or -f.")
        sys.exit(1)


if __name__ == "__main__":
    command_check()
    flags_check()
