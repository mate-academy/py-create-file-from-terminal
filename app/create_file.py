import os
import sys

from datetime import datetime


def create_file() -> None:
    dir_path = ""
    f_check = False
    if "-f" in sys.argv:
        f_check = True

    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d") + 1
        dir_path = os.path.join(*sys.argv[dir_index:])
        if f_check:
            dir_path = dir_path.split("-f")[0]
        os.makedirs(dir_path, exist_ok=True)

    if f_check:
        file_index = sys.argv.index("-f") + 1
        file_path = dir_path + sys.argv[file_index]
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, "a") as file:
            line_number = 1
            file.write(f"{timestamp}\n")
            while True:
                line = input("Enter content line: ")
                if line == "stop":
                    break
                file.write(f"{line_number} {line}\n")
                line_number += 1
            file.write("\n")


if __name__ == "__main__":
    create_file()
