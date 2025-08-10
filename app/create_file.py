from datetime import datetime
import os
import sys


args = sys.argv[1:]


def create_dirs(path_name: str) -> None:
    if not os.path.exists(path_name):
        os.makedirs(path_name)


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file_out:
        line_number = 1
        print(datetime.strftime(datetime.now(), "%y-%m-%d %H:%M:%S"),
              file=file_out)
        while True:
            word = input("Enter content line: ")
            if word == "stop":
                break
            print(line_number, word, file=file_out)
            line_number += 1


if __name__ == "__main__":
    if "-d" in args and "-f" in args:
        create_dirs(os.path.join(*args[1:-2]))
        create_file(os.path.join(os.path.join(*args[1:-2]), args[-1]))

    elif "-d" in args:
        create_dirs(os.path.join(*args[1:]))

    elif "-f" in args:
        create_file(args[1])
