import sys
import os
from datetime import datetime


def create_new_file_or_add_to_file() -> None:
    args = sys.argv[1:]

    has_d = "-d" in args
    has_f = "-f" in args

    dir_path = ""

    if has_d:
        d_index = args.index("-d")
        directories = []
        for name in args[d_index + 1:]:
            if name.startswith("-"):
                break
            directories.append(name)
        dir_path = os.path.join(*directories)
        os.makedirs(dir_path, exist_ok=True)

    file_path = None
    if has_f:
        f_index = args.index("-f")
        filename = args[f_index + 1]
        if has_d:
            file_path = os.path.join(dir_path, filename)
        else:
            file_path = filename

    list_line = []
    while True:
        line_user = input("Enter content line: ")
        if line_user.lower() == "stop":
            break
        list_line.append(line_user)

    if not list_line:
        return

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if file_path:
        with open(file_path, "a") as new_file:
            new_file.write(f"\n{timestamp}\n")
            for i, line in enumerate(list_line, start=1):
                new_file.write(f"{i} {line}\n")


if __name__ == "__main__":
    create_new_file_or_add_to_file()