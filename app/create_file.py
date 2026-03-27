import sys
import os
from datetime import datetime


def file_writer(name: str) -> None:
    with open(name, "a") as file_open:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_open.write(current_time + "\n")
        line = 1

        while True:
            content = input("Enter content line: ")

            if content.lower() == "stop":
                break
            file_open.write(f"{line} {content}\n")
            line += 1

        file_open.write("\n")


def create_file(args: list) -> None:
    dir_path = "."
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        dir_parts = []

        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dir_parts.append(arg)

        if dir_parts:
            dir_path = os.path.join(*dir_parts)
            os.makedirs(dir_path, exist_ok=True)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]
        else:
            print("Error: No file name provided after -f")
            return
    else:
        print("Error: No -f flag provided")
        return

    file_path = os.path.join(dir_path, file_name)
    file_writer(file_path)


if __name__ == "__main__":
    create_file(sys.argv[1:])
