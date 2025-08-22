import sys
import os
from datetime import datetime


cmd_line = sys.argv
cmd_line.pop(0)
file_to_write = None
skip_next_f = False


def file_writer(file_path: str) -> None:
    file_exists = os.path.exists(file_path)
    with open(f"{file_path}", "a") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")
        time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time_stamp}\n")
        line_number = 1
        while True:
            line = input(f"{file_path} Enter content line: ")
            if line != "stop":
                file.write(f"{line_number} {line}\n")
                line_number += 1
            else:
                break
    global file_to_write
    file_to_write = None


def create_dirs_and_files(line: list, file_path: str | None) -> None:
    path = os.getcwd()
    for index, directory in enumerate(line):
        if directory == "-f" and not file_path and (index + 1) != len(line):
            file_path = line[index + 1]
            global skip_next_f
            skip_next_f = True
            break
        if directory in ("-f", "-d"):
            break
        path = os.path.join(path, directory)
    if path != os.getcwd():
        os.makedirs(path, exist_ok=True)
    if file_path:
        file_writer(os.path.join(path, file_path))


for i, item in enumerate(cmd_line):
    if item in ("-f", "-d") and (
        i + 1 == len(cmd_line) or cmd_line[i + 1] in ("-f", "-d")
    ):
        raise ValueError(f"Empty {item} flag argument")
    if item == "-f" and not skip_next_f:
        if file_to_write:
            file_writer(os.path.join(os.getcwd(), file_to_write))
        file_to_write = cmd_line[i + 1]
    if item == "-f" and i - len(cmd_line) == -2 and file_to_write:
        file_writer(os.path.join(os.getcwd(), file_to_write))
    if item == "-f":
        skip_next_f = False
    elif item == "-d":
        create_dirs_and_files(cmd_line[i + 1 :], file_to_write)
