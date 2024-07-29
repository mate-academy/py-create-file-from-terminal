import os
import argparse
from datetime import datetime


def create_file() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", type=str, nargs="+")
    parser.add_argument("-f", "--filename", type=str)
    args = parser.parse_args()

    if args.directory:
        directory_path = os.path.join(*args.directory)
        os.makedirs(directory_path, exist_ok=True)
    else:
        directory_path = os.getcwd()

    if args.filename:
        filepath = os.path.join(directory_path, args.filename)

        with open(filepath, "a") as file:
            file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
            i = 1
            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    file.write("\n")
                    break
                file.write(f"{i} " + content + "\n")
                i += 1


create_file()
