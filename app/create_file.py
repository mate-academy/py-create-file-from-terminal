import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    if not os.path.exists(directory):
        os.makedirs(directory)
    file_path = os.path.join(directory, filename)
    print(file_path)
    with open(file_path, "w") as file:
        file.write(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d") + 1
        file_index = args.index("-f") + 1

        directory = os.path.join(*args[dir_index:file_index - 1])
        os.makedirs(directory, exist_ok=True)

        filename = args[file_index]
        create_file(directory, filename)

    elif "-d" in args:
        dir_index = args.index("-d") + 1
        directory = os.path.join(*args[dir_index:])
        os.makedirs(directory, exist_ok=True)

    elif "-f" in args:
        file_index = args.index("-f") + 1
        filename = args[file_index]
        create_file(".", filename)
