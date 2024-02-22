import os
import sys
from datetime import datetime
TIME_FORMAT = "%Y-%m-%d %H:%M:%S"


def create_file(path: str):
    with open(path, "a") as file:
        timestamp = datetime.now().strftime(TIME_FORMAT)
        file.write(timestamp + "\n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            file.write(f"{line_number} {content}\n")
            line_number += 1


def create_dir(path: str):
    try:
        os.makedirs(path)
        print("Created directory:", path)
    except FileExistsError:
        print("Can't create directory")


def main():
    args = sys.argv
    if "-d" in args and "-f" in args:
        dir_path = []
        for index in range(args.index("-d") + 1, len(args)):
            if args[index] == "-f":
                break
            dir_path.append(args[index])
        dir_path = os.path.join(*dir_path)
        create_dir(dir_path)
        file_name = os.path.join(dir_path, args[args.index("-f") + 1])
        create_file(file_name)
        return
    if "-d" in args:
        dir_path = args[args.index("-d") + 1::]
        print(dir_path)
        dir_path = os.path.join(*dir_path)
        create_dir(dir_path)
    if "-f" in args:
        file_name = args[args.index("-f") + 1]
        create_file(file_name)


main()
