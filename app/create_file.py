import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    file_exists = os.path.exists(file_path)
    start_line = 1

    if file_exists and os.path.getsize(file_path) > 0:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in reversed(lines):
                if line.strip() and line[0].isdigit():
                    start_line = int(line.split()[0]) + 1
                    break

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            with open(file_path, "rb") as f_check:
                f_check.seek(-1, os.SEEK_END)
                last_char = f_check.read(1)
                if last_char != b"\n":
                    file.write("\n")
            file.write("\n")
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        number_of_line = start_line
        while True:
            input_line = input("Enter content line: ")
            if input_line.lower() == "stop":
                break
            file.write(f"{number_of_line} {input_line}\n")
            number_of_line += 1


def find_path_from_terminal() -> None:
    args = sys.argv[1:]
    dir_path = ""
    if "-d" in args:
        index_d = args.index("-d") + 1
        dirs = []
        while index_d < len(args) and not args[index_d].startswith("-"):
            dirs.append(args[index_d])
            index_d += 1
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
    if "-f" in args:
        index_f = args.index("-f") + 1
        if index_f < len(args):
            filename = args[index_f]
            file_path = os.path.join(dir_path, filename)
            create_file(file_path)


if __name__ == "__main__":
    find_path_from_terminal()
