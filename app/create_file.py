import os
import datetime
import sys


def create_directories(path: str) -> None:
    if path != "":
        os.makedirs(path, exist_ok=True)


def create_file(path: str) -> None:
    mode = "w"
    if os.path.isfile(path):
        mode = "a"
    with open(path, mode) as f:
        f.write(str(datetime.datetime.strftime(
            datetime.datetime.now(),
            "%Y-%m-%d %H:%M:%S")) + "\n"
        )
        line_num = 1
        input_text = input("Enter content line: ")
        while input_text != "stop":
            f.write(str(line_num) + " " + input_text + "\n")
            line_num += 1
            input_text = input("Enter content line: ")
        f.write("\n")


def create_file_or_directory() -> None:
    path = sys.argv[1:]
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
        if idx + 1 < len(path):
            if path[idx] == "-f":
                file_path = os.path.join(directories_path, path[idx + 1])
                create_file(file_path)
    elif path[0] == "-f":
        if len(path) < 2:
            print("Please enter a file path")
            return

        directories_path = ""
        if len(path) > 2:
            if path[2] == "-d":
                idx = 3
                while idx < len(path):
                    directories_path = os.path.join(
                        directories_path,
                        path[idx]
                    )
                    idx += 1
                create_directories(directories_path)
        directories_path = os.path.join(directories_path, path[1])
        create_file(directories_path)
