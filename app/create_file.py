import os
import sys
from datetime import datetime


# first of all we create function, which returns path
# string transforming it from input in terminal
def create_directory(dir_path: list) -> str:
    full_path = os.path.join(os.getcwd(), *dir_path)
    os.makedirs(full_path, exist_ok=True)
    return full_path


def write_to_file(file_path: str, max_lines: int = 10) -> None:
    with open(file_path, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{timestamp}\n")

        for num in range(1, max_lines + 1):
            line = input(f"Enter content line (1-{max_lines}): ")
            if line.lower() == "stop":
                break
            f.write(f"{num} {line}\n")


def main() -> None:
    args = sys.argv

    if "-d" in args:
        d_index = args.index("-d")
        if "-f" in args:
            f_index = args.index("-f")
            dir_path = args[d_index + 1:f_index]
            file_name = args[f_index + 1]
        else:
            dir_path = args[d_index + 1:]
            file_name = None
    elif "-f" in args:
        f_index = args.index("-f")
        dir_path = []
        file_name = args[f_index + 1]
    else:
        print("How to write: create_file.py -d dir1 dir2 -f filename")
        return

    full_dir_path = create_directory(dir_path) if dir_path else os.getcwd()

    if file_name:
        # os.path.join("A", "B", "C") we join parts of the
        # path to the path itself.
        # This happens when we press -d
        # we use context manager to create the file in mode append
        full_file_name = os.path.join(full_dir_path, file_name)
        write_to_file(full_file_name)
        print(f"File {file_name} updated")
    elif dir_path:
        print(f"Directory {dir_path} created")
