import os
import sys
from datetime import datetime


def create_file():
    if "-f" in sys.argv and "-d" in sys.argv:
        directories = sys.argv[sys.argv.index("-d") + 1: sys.argv.index("-f")]
        file = sys.argv[sys.argv.index("-f") + 1]
        file_name = os.path.join(create_directory(directories), file)
        file_generator(file_name)
    elif "-d" in sys.argv:
        directories = sys.argv[sys.argv.index("-d") + 1:]
        create_directory(directories)
    elif "-f" in sys.argv:
        file = sys.argv[sys.argv.index("-f") + 1]
        file_generator(file)


def create_directory(directories):
    path = os.getcwd()
    for directory in directories:
        path = os.path.join(path, directory)
    os.makedirs(path)
    return path


def file_generator(file):
    with open(file, "a") as f:
        now = datetime.now()
        f.write(now.strftime("%m-%d-%Y %H:%M:%S") + "\n")
        i = 1
        while True:
            content = input("Enter content line: ")
            if content != "stop":
                f.write(f"{str(i)} content \n")
                i += 1
            else:
                break


if __name__ == "__main__":
    create_file()
