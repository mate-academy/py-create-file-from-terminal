import sys
import os
from datetime import datetime


def make_directory(path: str) -> str:
    os.makedirs(path, exist_ok=True)
    return path


def create_file(file_path: str) -> None:
    content = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        line = input("Enter content line: ")
        if line.strip().lower() == "stop":
            break
        content.append(line)

    with open(file_path, "a", encoding="utf-8") as f:
        f.write(timestamp + "\n")
        for i, line in enumerate(content, 1):
            f.write(f"{i} {line}\n")
        f.write("\n")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py -d [dirs] -f [file]")
        return

    dir_path, file_name = "", ""
    if "-d" in args:
        d_index = args.index("-d") + 1
        if "-f" in args:
            f_index = args.index("-f")
            dir_parts = args[d_index:f_index]
        else:
            dir_parts = args[d_index:]
        dir_path = make_directory(os.path.join(*dir_parts))

    if "-f" in args:
        f_index = args.index("-f") + 1
        file_name = args[f_index]
        full_path = os.path.join(dir_path, file_name) \
            if dir_path else file_name
        create_file(full_path)


if __name__ == "__main__":
    main()
