import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    dir_path_parts = []
    file_name = None

    if "-d" in args and "-f" in args:
        d_index = args.index("-d")
        f_index = args.index("-f")

        if d_index < f_index:
            dir_path_parts = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
        else:
            file_name = args[f_index + 1]
            dir_path_parts = args[d_index + 1:]
    elif "-d" in args:
        d_index = args.index("-d")
        dir_path_parts = args[d_index + 1:]
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    dir_path = os.path.join(*dir_path_parts) if dir_path_parts else ""

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if file_name:
        file_path = os.path.join(dir_path, file_name)

        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, "a") as file:
            file.write(f"{timestamp}\n")
            for index, line in enumerate(lines, start=1):
                file.write(f"{index} {line}\n")
            file.write("\n")


if __name__ == "__main__":
    create_file()
