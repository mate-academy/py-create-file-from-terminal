import sys
import os
from datetime import datetime


args_from_terminal = sys.argv[1:]


def create_directory(args: list) -> str:
    if args[0] == "-d":
        for directory in args[1:]:
            if directory == "-f":
                break
            if os.path.isdir(directory):
                os.chdir(directory)
            else:
                os.mkdir(directory)
                os.chdir(directory)
    return os.getcwd()


def create_and_write_file(args: list) -> None:
    if "-f" in args:
        page_number = 1
        filename = args[-1]
        os.chdir(create_directory(args_from_terminal))
        with open(filename, "a") as new_file:
            new_file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
            while True:
                input_text = input("Enter content line: ")
                if input_text == "stop":
                    break
                new_file.write(f"{page_number} {input_text}\n")
                page_number += 1
    else:
        create_directory(args_from_terminal)


if __name__ == "__main__":
    create_and_write_file(args_from_terminal)
