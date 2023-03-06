import os
import argparse
import datetime
from typing import Any


def create_directory(args: Any) -> Any:
    dir_path = os.path.join(*args.directory)
    os.makedirs(dir_path, exist_ok=True)
    return dir_path


def write_content(file_path: Any) -> Any:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(now + "\n")
        line_index = 1
        while True:
            line = input(f"Enter content line: {line_index} ")
            if line.lower() == "stop":
                break
            file.write(f"{line_index} {line}\n")
            line_index += 1
        file.write("\n")


parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", nargs="+", help="directory path")
parser.add_argument("-f", "--file", help="file name")
args = parser.parse_args()

if args.directory:
    dir_path = create_directory(args)
    if args.file:
        file_path = os.path.join(dir_path, args.file)
        write_content(file_path)

elif args.file:
    write_content(args.file)

else:
    print("Error: Enter -d or -f flag.")
