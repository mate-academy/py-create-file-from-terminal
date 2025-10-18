import os
import datetime
import sys


def create_directories(path: str) -> None:
    if not os.path.exists(path) and path != "":
        os.makedirs(path)


def create_file(path: str) -> None:
    mode = "w"
    if os.path.isfile(path):
        mode = "a"
    with open(path, mode) as f:
        f.write(str(datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")) + "\n")
        line_num = 1
        input_text = input("Enter content line: ")
        while input_text != "stop":
            f.write(str(line_num) + " " + input_text + "\n")
            line_num += 1
            input_text = input("Enter content line: ")
        f.write("\n")


def create_file_or_directory() -> None:
    sys.argv.remove(sys.argv[0])
    path = sys.argv
    if not path:
        return
    if path[0] == "-d":
        directories_path = ""
        idx = 1
        while idx < len(path):
            if path[idx] == "-f":
                break
            directories_path = os.path.join(directories_path, path[idx])
            idx += 1
        create_directories(directories_path)
        if idx != len(path):
            create_directories(directories_path)
            if path[idx] == "-f":
                file_path = os.path.join(directories_path, path[idx + 1])
                create_file(file_path)
    elif path[0] == "-f":
        create_file(path[1])

create_file_or_directory()