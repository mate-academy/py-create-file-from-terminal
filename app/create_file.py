import datetime

from os import makedirs, path, getcwd
from sys import argv

class InvalidArguments(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)

def get_directories() -> list:
    directories = []

    index_of_option = argv.index("-d")

    for i in range(index_of_option + 1, len(argv)):
        if argv[i] == "-f":
            break
        directories.append(argv[i])

    if not directories:
        raise InvalidArguments("Arguments after -d option are missing!")
    return directories

def get_file_name() -> str:
    index_of_option = argv.index("-f")

    if index_of_option == len(argv) - 1 or argv[index_of_option + 1] == "-d":
        raise InvalidArguments("Argument after -f option is missing!")
    return argv[index_of_option + 1]

def create_file():
    if "-d" in argv:
        directories_path = path.join(getcwd(), *get_directories())

        makedirs(directories_path, exist_ok=True)

        if "-f" in argv:
            absolute_path = path.join(directories_path, get_file_name())
            write_file(absolute_path)

    elif "-f" in argv:
        absolute_path = path.join(getcwd(), get_file_name())
        write_file(absolute_path)
    else:
        raise InvalidArguments("No option is specified!")

def write_file(path_to_the_file: str) -> None:
    with open(path_to_the_file, "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        f.write("\n")

        line_count = 1
        while True:
            input_text = ""
            input_text = input("Enter content line: ")
            if input_text == "stop":
                f.write("\n")
                break

            f.write(f"{line_count} {input_text}\n")
            line_count += 1

if __name__ == "__main__":
    create_file()
