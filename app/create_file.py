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
        if mode == "a":
            read_f = open(path, "r")
            content = read_f.read()
            read_f.close()
            if not content.endswith("\n"):
                f.write("\n")

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

    dir_flag = path.index("-d")
    file_flag = path.index("-f")

    directories_path = ""
    if dir_flag != -1:
        idx = dir_flag + 1
        while idx < len(path):
            if path[idx] == "-f":
                break
            directories_path = os.path.join(directories_path, path[idx])
            idx += 1
        if directories_path == "":
            print("Please enter a directory path")
            return
        create_directories(directories_path)

    if file_flag != -1:
        if file_flag + 1 >= len(path) or path[file_flag + 1].startswith("-"):
            print("Please enter a file path")
            return
        file_path = os.path.join(directories_path, path[file_flag + 1])
        create_file(file_path)


if __name__ == "__main__":
    create_file_or_directory()
