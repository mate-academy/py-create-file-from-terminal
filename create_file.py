import os
import sys
from datetime import datetime


def create_file(directory, filename, content):
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(os.path.join(directory, filename), "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for i, line in enumerate(content, start=1):
            f.write(f"{i} {line}\n")


def main():
    args = sys.argv[1:]
    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        directory = os.path.join(*args[dir_index + 1: file_index])
        filename = args[file_index + 1]
    elif "-d" in args:
        directory = os.path.join(*args[args.index("-d") + 1:])
        filename = input("Enter filename: ")
    elif "-f" in args:
        directory = "."
        filename = args[args.index("-f") + 1]
    else:
        return

    content = []
    while True:
        line = input("Enter content line: ")
        if line.lower() == "stop":
            break
        content.append(line)

    create_file(directory, filename, content)


if __name__ == "__main__":
    main()
