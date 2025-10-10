import os
import sys
from datetime import datetime


def create_directories(path_parts):
    path = os.path.join(*path_parts)
    os.makedirs(path, exist_ok=True)
    print(f"Directory created: {path}")
    return path


def create_file(file_path):
    if os.path.exists(file_path):
        print(f"File already exists: {file_path}")
    else:
        print(f"File created: {file_path}")
    return open(file_path, "a")


def write_content_to_file(file):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(f"\n{timestamp}\n")
    line_number = 1
    while True:
        content = input(f"Enter content line ({line_number}): ")
        if content.lower() == "stop":
            break
        file.write(f"{line_number} {content}\n")
        line_number += 1
    file.close()
    print("Content written to file.")


def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python create_file.py [-d dir1 dir2 ...] [-f filename]")
        return

    directory_path = []
    file_name = None

    if "-d" in args:
        d_index = args.index("-d")
        directory_path = args[d_index + 1 :]
        if "-f" in directory_path:
            f_index = directory_path.index("-f")
            file_name = directory_path[f_index + 1]
            directory_path = directory_path[:f_index]
    elif "-f" in args:
        f_index = args.index("-f")
        file_name = args[f_index + 1]

    if directory_path:
        dir_path = create_directories(directory_path)
    else:
        dir_path = os.getcwd()

    if file_name:
        file_path = os.path.join(dir_path, file_name)
        with create_file(file_path) as file:
            write_content_to_file(file)


if __name__ == "__main__":
    main()
