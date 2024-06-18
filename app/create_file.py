import os
import sys
from datetime import datetime


def create_file(directory: str = None, filename: str = None) -> None:
    if directory:
        dir_path = os.path.join(*directory)
        os.makedirs(dir_path, exist_ok=True)
        if filename:
            file_path = os.path.join(dir_path, filename)
            create_or_append_file(file_path)
    elif filename:
        create_or_append_file(filename)
    else:
        print("Please provide either a directory path "
              "(-d flag) or a filename (-f flag).")


def create_or_append_file(file_path: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content = []
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            content = f.readlines()
    print(f"Enter content for {file_path} (type 'stop' to finish):")
    line = input("Enter content line: ")
    while line != "stop":
        content.append(line + "\n")
        line = input("Enter content line: ")
    with open(file_path, "w") as f:
        f.write(timestamp + "\n")
        for i, line in enumerate(content, start=1):
            f.write(f"{i} {line}")


if __name__ == "__main__":
    args = sys.argv[1:]
    directory = None
    filename = None
    if "-d" in args:
        index = args.index("-d")
        directory = args[index + 1:]
        if "-f" in args:
            filename = args[args.index("-f") + 1]
    elif "-f" in args:
        filename = args[args.index("-f") + 1]

    create_file(directory, filename)
