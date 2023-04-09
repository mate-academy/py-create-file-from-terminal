import os
import sys
from datetime import datetime


def create_file() -> None:
    args = sys.argv[1:]

    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        dir_path = os.path.join(*args[dir_index + 1:])

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        file_path = os.path.join(dir_path, file_name)

    elif "-d" in args:
        dir_index = args.index("-d")
        dir_path = os.path.join(*args[dir_index + 1:])

        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        return

    elif "-f" in args:
        file_index = args.index("-f")
        file_name = args[file_index + 1]
        file_path = file_name
    else:
        print("Please specify either the '-d' "
              "flag to create a directory or the '-f' flag to create a file.")
        return

    content = []
    line = input("Enter content line: ")
    while line != "stop":
        content.append(line)
        line = input("Enter content line: ")

    if os.path.exists(file_path):
        with open(file_path, "a") as file:
            file.write("\n")
            file.write("\n".join(content))
    else:
        with open(file_path, "w") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp + "\n")
            for i, line in enumerate(content):
                file.write(f"{i+1} {line}\n")


create_file()
