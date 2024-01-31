import os
import sys
from datetime import datetime


print("Enter: ", sys.argv)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_path(directories: list) -> str:
    path = os.path.join(*directories)
    return path


def create_directory(directory_path: str) -> None:
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
    print("Directory exists already!")


def create_file(file_name: str) -> None:

    with open(file_name, "a") as file:

        file.write(f"{timestamp} \n")
        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_num} {line} \n")
            line_num += 1


def main():
    if "-d" in sys.argv:
        dir_index = sys.argv.index("-d")
        directory_path = os.path.join(*sys.argv[dir_index + 1:])
        create_directory(directory_path)

    if "-f" in sys.argv:
        file_index = sys.argv.index("-f")
        file_name = sys.argv[file_index + 1]
        create_file(file_name)


if __name__ == '__main__':
    main()
