import datetime
import os.path
import sys


def read_file_path() -> (list, int):
    file_path = []
    next_flag_position = argv_length - 1
    for i in range(2, argv_length):
        if sys.argv[i] != "-f":
            file_path.append(sys.argv[i])
        else:
            next_flag_position = i
            break
    return file_path, next_flag_position


def read_file_name() -> str:
    return sys.argv[argv_length - 1]


def read_input() -> list:
    content = []
    while 1:
        new_line = input("Enter content line: ")
        if new_line == "stop":
            break
        content.append(new_line)
    return content


def write_info(file_to_write_info: str, content: list) -> None:
    with open(file_to_write_info, "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%I:%M%p %d/%B/%Y')}\n")
        for i in range(len(content)):
            f.write(f"{i + 1} Line{i+1} {content[i]}\n")
        f.write("\n")


if __name__ == "__main__":
    f_flag_position = 0
    argv_length = len(sys.argv)
    directory_path = []
    file_name = ""

    if sys.argv[1] == "-d":
        directory_path, f_flag_position = read_file_path()
    else:
        file_name = read_file_name()
    if f_flag_position != argv_length - 1:
        file_name = read_file_name()

    path = ""
    if directory_path:
        path = os.path.join(*directory_path)
        os.makedirs(path, exist_ok=True)
    if file_name:
        write_info(os.path.join(path, file_name), read_input())
