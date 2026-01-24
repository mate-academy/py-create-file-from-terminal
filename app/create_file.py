import os
import sys
from datetime import datetime


def create_directory(directory: str) -> None:
    os.makedirs(directory, exist_ok=True)


def write_file(directory: str, filename: str) -> None:
    filepath = os.path.join(directory, filename)
    with open(filepath, "a") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_number} {line}\n")
            line_number += 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_file.py [-d dir1 dir2] [-f filename]")
        sys.exit(1)

    directory = ""
    filename = ""
    d_flag = False
    f_flag = False

    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "-d":
            d_flag = True
            i += 1
            dir_parts = []
            while i < len(sys.argv) and not sys.argv[i].startswith("-"):
                dir_parts.append(sys.argv[i])
                i += 1
            directory = os.path.join(*dir_parts)
        elif sys.argv[i] == "-f":
            f_flag = True
            filename = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    if d_flag and not f_flag:
        create_directory(directory)
    elif f_flag and not d_flag:
        write_file(os.getcwd(), filename)
    elif d_flag and f_flag:
        create_directory(directory)
        write_file(directory, filename)
