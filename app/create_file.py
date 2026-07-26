import os
import sys
from datetime import datetime


def create_directory(dirs: list) -> None:
    path = os.path.join(*dirs)
    os.makedirs(path)


def create_file(filename: str) -> None:
    if os.path.exists(filename):
        append_write = "a"
    else:
        append_write = "w"
    with open(filename, append_write) as file:
        now = datetime.now()
        file.write(now.strftime("%Y-%m-%d, %H:%M:%S\n"))
        content_list = []
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                break
            content_list.append(input_line)
        for index, value in enumerate(content_list):
            file.write(f"{index + 1} {value}\n")


if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        print("Invalid command")
    if "-d" in args and "-f" not in args:
        index_d = args.index("-d")
        dirs = args[index_d + 1:]
        create_directory(dirs)
    elif "-f" in args and "-d" not in args:
        index_f = args.index("-f")
        filename = args[index_f + 1]
        create_file(filename)
    elif "-d" in args and "-f" in args:
        index_d = args.index("-d")
        index_f = args.index("-f")
        dirs = args[index_d + 1: index_f]
        filename = args[index_f + 1:]
        if dirs:
            create_directory(dirs)
        path = os.path.join(*dirs, *filename)
        create_file(str(path))
    else:
        print("Invalid arguments")
