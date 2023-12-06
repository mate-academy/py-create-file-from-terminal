import os
import sys
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path)


def python_create_file(directory: str, name: str) -> None:
    path_to_file = os.path.join(directory, name)

    with open(path_to_file, "w") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        print("Enter content line")

        line_number = 1
        while True:
            line = input()
            if line.lower() == "stop":
                break

            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        path = os.path.join(*sys.argv[dir_index:])
        create_directory(path)
    elif "-f" in sys.argv:
        filename_index = sys.argv.index("-f") + 1
        python_create_file(os.getcwd(), sys.argv[filename_index])
    else:
        print("Invalid arguments")


main()
