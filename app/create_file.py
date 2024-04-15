import datetime

import os

import sys


def create_directory(path_parts):
    directory_path = os.path.join(*path_parts)
    os.makedirs(directory_path, exist_ok=True)


def create_file(file_name, path_parts=None):
    if path_parts is not None:
        directory_path = os.path.join(*path_parts)
        os.makedirs(directory_path, exist_ok=True)
        full_path = os.path.join(directory_path, file_name)
    else:
        full_path = file_name

    file_exists = os.path.isfile(full_path)

    with open(full_path, 'a' if file_exists else 'w') as file:
        file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + '\n')
        line = ""
        line_number = 0
        while True:
            line_in_cycle = input("Enter content line: ")
            if line_in_cycle == "stop":
                break
            line_number += 1
            line += f"{line_number} {line_in_cycle} \n"

        file.write(line)


def main():
    args = sys.argv[1:]
    if "-d" in args and "-f" in args:
        dir_index = args.index("-d")
        file_index = args.index("-f")
        if dir_index < file_index:
            path_parts = args[dir_index + 1: file_index]
            file_name = args[file_index + 1]
            create_directory(path_parts)
            create_file(file_name, path_parts)
        else:
            path_parts = args[dir_index + 1:]
            file_name = args[file_index + 1:dir_index]
            print(file_name, path_parts)
            create_directory(path_parts)
            create_file(file_name, path_parts)
    elif "-d" in args and "-f" not in args:
        create_directory(args[1:])
    elif "-f" in args and "-d" not in args:
        create_file(args[args.index("-f") + 1])


if __name__ == "__main__":
    main()
