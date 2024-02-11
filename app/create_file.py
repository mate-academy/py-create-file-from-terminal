import os
import argparse
from datetime import datetime


def create_file(dir_path: str, file_name: str) -> None:
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, file_name),
              "a" if os.path.exists(os.path.join(dir_path,
                                                 file_name)) else "w") as f:
        print("Enter content line by line, type 'stop' to end:")
        f.write(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n")
        line_num = 1
        while True:
            line = input()
            if line.lower() == "stop":
                break
            f.write(str(line_num) + " " + line + "\n")
            line_num += 1


def create_directory(dir_path: str) -> None:
    os.makedirs(dir_path, exist_ok=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="*", help="Create directory")
    parser.add_argument("-f", "--file", nargs=2, help="Create file with content")
    args = parser.parse_args()

    if args.directory:
        create_directory(os.path.join(*args.directory))
    if args.file:
        dir_path, file_name = args.file
        create_file(dir_path, file_name)
