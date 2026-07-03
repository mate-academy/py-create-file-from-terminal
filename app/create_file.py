import os
import datetime
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("-f", dest="file_name", required=False)
parser.add_argument("-d", dest="dir_path", nargs="+", required=False)
args = parser.parse_args()


def create_file_in_directory() -> None:
    if args.dir_path and args.file_name:
        create_directory(args.dir_path)
        create_file(args.dir_path)
    elif args.dir_path:
        create_directory(args.dir_path)
    elif args.file_name:
        create_file([])


def create_directory(path: list) -> None:
    os.makedirs(os.path.join(*path), exist_ok=True)


def create_file(path: list) -> None:
    file_path = os.path.join(*path, args.file_name)
    with open(file_path, "a") as f:
        if os.path.getsize(file_path) > 0:
            f.write("\n\n")
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        line_num = 0
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            line_num += 1
            f.write(f"\n{str(line_num)} {line}")


create_file_in_directory()
