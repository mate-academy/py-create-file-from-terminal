import argparse
import os
from datetime import datetime


def write_content(path: str = None, file_name: str = None) -> None:
    input_count = 0

    if path is None:
        path = os.getcwd()
    else:
        os.makedirs(path)

    if file_name:
        with open(path + "/" + file_name, "a") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

            while True:
                content = input("Enter content line: ")
                if content == "stop":
                    break
                input_count += 1
                f.write(str(input_count) + " " + content + "\n")


def create_file() -> None:
    parser = argparse.ArgumentParser(
        prog="Create File",
        description="This app creates file from yours terminal input"
    )

    parser.add_argument("-d", dest="create_path", type=str)
    parser.add_argument("-f", dest="file_name", type=str)

    args = parser.parse_args()

    write_content(args.create_path, args.file_name)
