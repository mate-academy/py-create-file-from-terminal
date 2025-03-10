import argparse
import os
import datetime


def create_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", nargs="*")
    parser.add_argument("-f", "--filename")

    args = parser.parse_args()
    full_path = os.getcwd()

    if args.directory:
        full_path = ""
        for directory in args.directory:
            full_path = os.path.join(full_path, directory)


    os.makedirs(full_path, exist_ok=True)

    path = os.path.join(full_path, args.filename)

    content = str
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if args.filename:
        with open(path, "a") as f:
            f.write(now + "\n")
            counter_lines = 0
            while content != "stop":
                counter_lines += 1
                content = input("Enter content line: ")
                f.write(f"{counter_lines} " + content + "\n")


if __name__ == "__main__":
    create_file()
