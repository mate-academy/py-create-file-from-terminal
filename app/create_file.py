from sys import argv
from os import makedirs, path
from datetime import datetime


def make_dirs(arguments: list) -> str | bytes:
    index_d = arguments.index("-d")
    if "-f" not in arguments or arguments.index("-f") < index_d:
        dirs = arguments[index_d + 1 :]
    else:
        dirs = arguments[index_d + 1 : arguments.index("-f")]
    path_file = path.join(*dirs)
    makedirs(path_file, exist_ok=True)
    return path_file


def write_file(arguments: list, path_file: str = "") -> None:
    index_f = arguments.index("-f")
    file_name = arguments[index_f + 1]
    file_dir = path.join(path_file, file_name)
    with open(file_dir, "a+") as file:
        if file.tell() > 0:
            file.write("\n")
        file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        i = 1
        while True:
            usr_input = input("Enter content line: ")
            if usr_input == "stop":
                break
            file.write(f"{i} {usr_input}\n")
            i += 1


if __name__ == "__main__":
    if "-d" in argv and "-f" in argv:
        write_file(argv, make_dirs(argv))
    elif "-f" in argv:
        write_file(argv)
    elif "-d" in argv:
        make_dirs(argv)
