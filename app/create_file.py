import sys
import os
from datetime import datetime


def create_file() -> None:
    sys_arg = sys.argv
    dir_path = ""
    if sys_arg.count("-d") == 1:

        start = sys_arg.index("-d")
        if sys_arg.count("-f") == 1:
            end = sys_arg.index("-f")
        else:
            end = len(sys_arg)

        for next_dir in sys_arg[start + 1:end]:
            dir_path = os.path.join(dir_path, next_dir)
        try:
            os.makedirs(dir_path)
        except FileExistsError:
            print(f"Dir or path {dir_path} already exists")
        except FileNotFoundError:
            print("Rename file")

    if sys_arg.count("-f") == 1:
        file_name = sys_arg[sys_arg.index("-f") + 1]
        if not dir_path:
            file_path = file_name
        else:
            file_path = os.path.join(dir_path, file_name)
        with open(file_path, "a") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            line_number = 1
            while True:
                line = input("Enter content line: ")
                if line.lower() != "stop":
                    f.write(f"{line_number} ")
                    f.write(line)
                    f.write("\n")
                    line_number += 1
                else:
                    f.write("\n")
                    break


if __name__ == "__main__":
    create_file()
