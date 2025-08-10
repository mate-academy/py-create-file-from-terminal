import os
from datetime import datetime
import sys


def create_file(file_name: str) -> None:
    with open(file_name, "a") as source_file:
        time_stamp = (datetime.now().strftime("%Y-%m-%d, %H:%M:%S") + "\n")
        source_file.write(f"{time_stamp} \n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                source_file.write("\n")
                break
            source_file.write(f"{line_number} {content} \n")
            line_number += 1


def create_file_and_directories() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = create_directories()
        file_name = os.path.join(*path, sys.argv[sys.argv.index("-f") + 1])
        create_file(file_name)
    elif "-d" in sys.argv:
        create_directories()
    elif "-f" in sys.argv:
        file_name = sys.argv[sys.argv.index("-f") + 1]
        create_file(file_name)


def create_directories() -> list:
    d_flag_index = sys.argv.index("-d")

    if "-f" in sys.argv:
        f_flag_index = sys.argv.index("-f")
        directories_list = sys.argv[d_flag_index + 1:f_flag_index]
    else:
        directories_list = sys.argv[d_flag_index + 1:]

    path = os.path.join(*directories_list)
    os.makedirs(path, exist_ok=True)
    return directories_list


if __name__ == "__main__":
    create_file_and_directories()
