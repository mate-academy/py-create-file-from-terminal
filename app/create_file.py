import os
import sys

from datetime import datetime


def create_file(file_name: str) -> None:
    with open(file_name, "a") as file:
        creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(creation_date + "\n")
        line_count = 1
        while True:
            content_line = input("Enter content line: ")
            if content_line == "stop":
                file.write("\n")
                break
            file.write(f"{line_count} {content_line}\n")
            line_count += 1


def create_dir(directories: list) -> None:
    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    os.chdir(path)


def process_terminal(args: list) -> None:
    if "-d" in args and "-f" in args:
        d_flag = args.index("-d")
        f_flag = args.index("-f")
        if d_flag < f_flag:
            create_dir(args[d_flag + 1: f_flag])
            create_file(args[-1])
        else:
            create_dir(args[d_flag + 1:])
            create_file(args[f_flag + 1])
    elif "-d" in args:
        _, d_flag, *dirs = args
        create_dir(dirs)
    elif "-f" in args:
        create_file(args[-1])


if __name__ == "__main__":
    arguments = sys.argv
    process_terminal(arguments)
