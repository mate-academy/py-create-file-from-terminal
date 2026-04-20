import os
import sys


def get_arguments():
    arguments = sys.argv
    directory_names = list()
    file_name = ""

    if "-d" in arguments:
        d_index = arguments.index("-d")
        for arg in arguments[d_index + 1:]:
            if arg == "-f":
                break
            directory_names.append(arg)

    if "-f" in arguments:
        f_index = arguments.index("-f")
        if f_index + 1 < len(arguments):
            file_name = arguments[f_index + 1]

    return directory_names, file_name


def main():
    folder_parts, name = get_arguments()

    if not name:
        print("No arguments (-f 'filename', -d 'dir1' 'dir2' -> dir1/dir2/filename)")
        return


if __name__ == "__main__":
    main()