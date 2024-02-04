import os
import sys
from datetime import datetime


def create_file(directory: str, filename: str) -> None:
    if directory and not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, filename), "a") as file:
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


def main() -> None:
    args = sys.argv[1:]
    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        if dir_index < file_index:
            directory = os.path.join(*args[dir_index + 1:file_index])
            filename = args[file_index + 1]
        else:
            print("Invalid arguments")
            return
    elif "-d" in args:
        directory = os.path.join(*args[args.index("-d") + 1:])
        filename = input("Enter file name: ")
    elif "-f" in args:
        directory = ""
        filename = args[args.index("-f") + 1]
    else:
        print("Invalid arguments")
        return
    create_file(directory, filename)


if __name__ == "__main__":
    main()
