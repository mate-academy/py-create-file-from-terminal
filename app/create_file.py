import os
import sys
from datetime import datetime


def create_file(directories: str, file_name: str) -> None:
    os.makedirs(directories, exist_ok=True)
    full_path = os.path.join(directories, file_name)
    mode = "w" if not os.path.exists(full_path) else "a"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line_number = 1
    with open(full_path, mode) as file:
        if mode == "a":
            file.write("\n\n")
        file.write(f"{timestamp}\n")
        while True:
            line = input("Enter content line: ")
            if line.lower().strip() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    list_of_arguments = sys.argv
    if "-f" in list_of_arguments and "-d" not in list_of_arguments:
        file_name = list_of_arguments[list_of_arguments.index("-f") + 1]
        directories = os.getcwd()
    elif "-d" in list_of_arguments and "-f" not in list_of_arguments:
        file_name = "file.txt"
        directories = os.path.join(
            os.getcwd(),
            *list_of_arguments[list_of_arguments.index("-d") + 1:]
        )
    elif "-d" in list_of_arguments and "-f" in list_of_arguments:
        if list_of_arguments.index("-f") > list_of_arguments.index("-d"):
            directories = os.path.join(
                os.getcwd(),
                *list_of_arguments[list_of_arguments.index("-d")
                                   + 1:list_of_arguments.index("-f")]
            )
        else:
            directories = os.path.join(
                os.getcwd(),
                *list_of_arguments[list_of_arguments.index("-d") + 1:]
            )
        file_name = list_of_arguments[list_of_arguments.index("-f") + 1]

    create_file(directories, file_name)


if __name__ == "__main__":
    main()
