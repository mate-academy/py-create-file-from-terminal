import sys
import os
from datetime import datetime
from pathlib import Path


def start_crate_file():
    directory = f"{Path(__file__).resolve().parent.parent}"
    time = datetime.now().strftime("%Y-%m-%d %I:%M:%S")
    content = f"{time}\n"
    count = 0
    while True:
        inp = input('Enter content line: ')
        if inp != "stop":
            count += 1
            content += str(count) + " " + inp + "\n"
        else:
            break

    argv = sys.argv
    if "-d" in argv and "-f" in argv:
        file_by_directory_and_file(argv, content, directory)
    if "-f" in argv:
        file_by_file(argv, content, directory)
    if "-d" in argv:
        file_by_directory(argv, content, directory)


def iterator_by_dir(argv, ind_d):
    for i in range(ind_d + 1, len(argv) - ind_d + 1):
        if argv[i] == "-f":
            break
        else:
            directory = directory + os.path.join(f"\\{argv[i]}")
            if os.path.isdir(directory):
                pass
            else:
                os.mkdir(directory)


def file_a_and_w(content, directory, file="file.txt"):
    directory = directory + os.path.join(f"\\{file}")
    if os.path.isfile(directory):
        with open(directory, "a") as f:
            f.write(content)
    else:
        with open(directory, "w") as f:
            f.write(content)


def file_by_directory_and_file(argv, content, directory):
    ind_d = argv.index("-d")
    ind_f = argv.index("-f")
    iterator_by_dir(argv, ind_d)
    file_a_and_w(content, directory, argv[ind_f + 1])


def file_by_file(argv, content, directory):
    ind = argv.index("-f")
    file_a_and_w(content, directory, argv[ind + 1])


def file_by_directory(argv, content, directory):
    ind_d = argv.index("-d")
    iterator_by_dir(argv, ind_d)
    file_a_and_w(content, directory)


if __name__ == '__main__':
    start_crate_file()
