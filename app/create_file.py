import os
import sys
from datetime import datetime


def create_file(name_file: str, dir_path: str | list) -> None:
    file_path = os.path.join(*dir_path, name_file)
    with open(f"{file_path}", "a") as my_file:
        time_now = datetime.now()
        forma = time_now.strftime("%Y-%m-%d %H:%M:%S")
        my_file.write(forma + "\n")
        count_line = 0
        info = input("Enter content line: ")
        while info != "stop":
            count_line += 1
            my_file.write(f"{count_line} {info}\n")
            info = input("Enter content line: ")
        my_file.write("\n")


def create_directory(name_dirs: str) -> None:
    os.makedirs(name_dirs, exist_ok=True)


def read_arguments() -> tuple[str, str]:
    args = sys.argv[1:]
    dir_names, file_names = "", ""
    if "-f" in args:
        index_file = args.index("-f") + 1
        file_names = args[index_file]
        del args[index_file - 1: index_file + 1]
    if "-d" in args:
        dir_names = args[1:]
    return dir_names, file_names


def main() -> None:
    dir_names, file_names = read_arguments()
    if dir_names:
        name_dir = os.path.join(*dir_names[:])
        create_directory(name_dir)
    if file_names:
        create_file(file_names, dir_names)


if __name__ == "__main__":
    main()
