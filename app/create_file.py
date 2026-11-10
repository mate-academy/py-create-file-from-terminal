import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]
    dir_parts = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        for arg in args[d_index + 1:]:
            if arg.startswith("-"):
                break
            dir_parts.append(arg)

    if "-f" in args:
        f_index = args.index("-f")
        if f_index + 1 < len(args):
            file_name = args[f_index + 1]

    target_dir = os.path.join(*dir_parts) if dir_parts else ""

    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    if file_name:
        file_path = (
            os.path.join(target_dir, file_name)
            if target_dir
            else file_name
        )
        file_exists_and_not_empty = (
            os.path.exists(file_path) and os.path.getsize(file_path) > 0
        )
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open(file_path, "a") as file_obj:
            if file_exists_and_not_empty:
                file_obj.write("\n")
            file_obj.write(f"{timestamp}\n")
            line_number = 1
            while True:
                try:
                    line = input("Enter content line: ")
                except EOFError:
                    break
                if line == "stop":
                    break
                file_obj.write(f"{line_number} {line}\n")
                line_number += 1


create_file()
