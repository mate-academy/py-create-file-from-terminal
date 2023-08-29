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


if __name__ == "__main__":
    if "-d" in sys.argv and "-f" in sys.argv:
        d_flag = sys.argv.index("-d")
        f_flag = sys.argv.index("-f")
        if d_flag < f_flag:
            create_dir(sys.argv[d_flag + 1: f_flag])
            create_file(sys.argv[-1])
        else:
            create_dir(sys.argv[d_flag + 1:])
            create_file(sys.argv[f_flag + 1])
    elif "-d" in sys.argv:
        _, d_flag, *dirs = sys.argv
        create_dir(dirs)
    elif "-f" in sys.argv:
        create_file(sys.argv[-1])
