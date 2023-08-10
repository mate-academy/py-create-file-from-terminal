import os
import datetime
import sys


def get_from_terminal() -> None:
    if "-d" in sys.argv and "-f" in sys.argv:
        path = create_directories()
        create_new_file(path)
    elif "-d" in sys.argv:
        create_directories()
    elif "-f" in sys.argv:
        path = []
        create_new_file(path)


def create_new_file(directories: list) -> None:
    name = sys.argv[sys.argv.index("-f") + 1]
    if len(directories) != 0:
        filename = os.path.join(*directories, name)
    else:
        filename = name

    with open(filename, "a") as source_file:
        time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{time_stamp} \n")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                source_file.write("\n")
                break
            source_file.write(f"{line_number} {content} \n")
            line_number += 1


def create_directories() -> list:
    d_flag_index = sys.argv.index("-d")

    if "-f" in sys.argv:
        f_flag_index = sys.argv.index("-f")
        directories = sys.argv[d_flag_index + 1:f_flag_index]
    else:
        directories = sys.argv[d_flag_index + 1:]

    path = os.path.join(*directories)
    os.makedirs(path, exist_ok=True)
    return directories


if __name__ == "__main__":
    get_from_terminal()
