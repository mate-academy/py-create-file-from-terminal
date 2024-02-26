import os
from sys import argv


def create_file():
    file_path = os.getcwd()
    if "-d" in argv:
        file_path = os.path.join(file_path, *argv[argv.index("-d") + 1:])
        create_change_dirs(file_path)


def create_change_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)
    os.chdir(path)


if __name__ == "__main__":
    create_file()
