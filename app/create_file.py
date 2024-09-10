from datetime import datetime
import os
import sys


def create_directories(directories: list) -> None:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)


def create_and_write_in_file(file_name: str) -> None:
    with open(file_name, "a") as file_in:
        file_in.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        line_number = 0

        while True:
            user_input = input("Enter content line: ")
            if user_input == "stop":
                file_in.write("\n")
                break
            line_number += 1
            file_in.write(f"{line_number} {user_input}\n")


def find_directories_and_file_name(args: list) -> tuple:
    directories = []
    file_name = None

    for i, arg in enumerate(args):
        if arg == "-f":
            file_name = args[i + 1]

        if arg == "-d":
            for possible_dir in args[i + 1:]:
                if possible_dir == "-f":
                    break
                directories.append(possible_dir)

    return directories, file_name


def main() -> None:
    directories, file_name = find_directories_and_file_name(sys.argv[1:])

    if file_name and directories:
        create_directories(directories)
        full_file_name = os.path.join(*directories, file_name)
        create_and_write_in_file(str(full_file_name))
    elif file_name:
        create_and_write_in_file(file_name)
    elif directories:
        create_directories(directories)


if __name__ == "__main__":
    main()
