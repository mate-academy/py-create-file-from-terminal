import sys
import os
from datetime import datetime


def create_directory(path: str) -> None:
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")


def create_file(file_path: str) -> None:
    with open(file_path, "a") as file:
        file.write(f"\n{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line.lower() == "stop":
                break
            file.write(f"{line_num} {line}\n")
            line_num += 1
        print(f"File updated: {file_path}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "-d" in args:
        d_index = args.index("-d")
        path = "/".join(args[d_index + 1:])
        create_directory(path)
        args = args[:d_index]

    if "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]
        file_path = file_name if not path else f"{path}/{file_name}"
        create_file(file_path)
