import os
from sys import argv
from directories import create_directories
from file_name import create_f


def main() -> None:
    if "-d" in argv and "-f" in argv:
        dir_index, file_index = argv.index("-d"), argv.index("-f")
        dir_path = str(os.path.join(*argv[dir_index + 1: file_index]))
        file_path = str(os.path.join(*argv[file_index + 1:]))

        create_directories(dir_path)
        create_f(file_path)
    elif "-d" in argv:
        create_directories(str(os.path.join(*argv[2:])))
    elif "-f" in argv:
        create_f(str(os.path.join(*argv[2:])))


if __name__ == "__main__":
    main()
