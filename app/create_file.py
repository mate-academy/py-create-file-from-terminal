import os
import sys
from datetime import datetime


def create_file() -> None:
    def validate_input(data: list[str]) -> None:
        if len(data[1:]) < 2:
            raise ValueError(f"Command must have min 2 elements, but got: "
                             f"{len(data[1:])}")
        if "-d" not in data[1] and "-f" not in data[1]:
            raise ValueError("The command was entered incorrectly. "
                             "The command must contain the '-d' or '-f' flag")

        if "-d" in data[1] and "-f" not in data:
            if len(data[2:]) < 1:
                raise ValueError("The command was entered incorrectly. "
                                 "Must contain directory path.")
        if "-f" in data[1]:
            if 1 < len(data[2:]) or 1 > len(data[2:]):
                raise ValueError(f"The command was entered incorrectly. "
                                 f"Must contain only 1 file name, "
                                 f"but got {len(data[2:])}")
            if "-d" in data:
                raise ValueError("The command was entered incorrectly. "
                                 "If you want use both flags (-d and -f), "
                                 "you must use first -d flag and then -f flag")

    def create_directory(directory: list) -> None:
        path_to_directory = os.path.join(*directory)
        if not os.path.exists(path_to_directory):
            os.makedirs(path_to_directory)

    def create_file(file_name: str) -> None:
        with open(file_name, "a") as file:
            file.write((datetime.now()).strftime("%Y-%m-%d %H:%M:%S") + "\n")
            while True:
                input_line = input("Enter content line: ")
                if input_line == "stop":
                    file.write("\n")
                    break
                file.write(input_line + "\n")

    validate_input(sys.argv)

    if "-d" not in sys.argv[1] and "-f" not in sys.argv[1]:
        create_directory(sys.argv[2:])
    if "-f" in sys.argv[1]:
        create_file(sys.argv[2])
    else:
        path = sys.argv[2:]
        path.remove("-f")

        create_directory(path[:-1])

        file_path = os.path.join(*path[:-1], path[-1])

        create_file(file_path)


if __name__ == "__main__":
    create_file()
