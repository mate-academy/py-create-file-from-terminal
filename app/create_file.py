import os
from datetime import datetime
import argparse


def create_directory(args):
    path = os.getcwd()
    for directory in args.directories:
        path = os.path.join(path, directory)
    os.makedirs(path)
    return path


def file_generator(args):
    with open(args.file_name, "a") as f:
        now = datetime.now()
        f.write(now.strftime("%m-%d-%Y %H:%M:%S") + "\n")
        i = 1
        while True:
            content = input("Enter content line: ")
            if content != "stop":
                f.write(str(i) + ' ' + content + "\n")
                i += 1
            else:
                break


def create_file():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", nargs='+', dest="directories")
    parser.add_argument("-f", dest="file_name")
    args = parser.parse_args()

    if args.directories and args.file_name:

        args.file_name = os.path.join(create_directory(args), args.file_name)
        file_generator(args)

    elif args.directories:
        create_directory(args)

    elif args.file_name:
        file_generator(args)


if __name__ == "__main__":
    create_file()
