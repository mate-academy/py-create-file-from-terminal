import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S\n"))
        number_of_line = 1
        while True:
            input_line = input("Enter content line: ")
            if input_line.lower() == "stop":
                file.write("\n")
                break
            file.write(f"{number_of_line} {input_line}\n")
            number_of_line += 1


def find_path_from_terminal() -> None:
    args = sys.argv[1:]
    dirs = []
    if "-d" in args:
        index_d = args.index("-d") + 1
        while index_d < len(args) and not args[index_d].startswith("-"):
            dirs.append(args[index_d])
            index_d += 1
        dir_path = os.path.join(*dirs)
        os.makedirs(dir_path, exist_ok=True)
    else:
        dir_path = ""
    if "-f" in args:
        index_f = args.index("-f") + 1
        if index_f < len(args):
            filename = args[index_f]
            file_path = os.path.join(dir_path, filename)
            create_file(file_path)


if __name__ == "__main__":
    find_path_from_terminal()
