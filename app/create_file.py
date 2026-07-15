import datetime
import os
import sys


def write_file(path: str) -> None:
    file_contents = ""
    line_num = 1
    while True:
        file_input = input("Enter content line: ")
        if file_input == "stop":
            break
        file_contents = f"{file_contents}{line_num} {file_input}\n"
        line_num += 1
    with open(path, "a+") as target_file:
        target_file.seek(0, 0)
        if target_file.read() != "":
            target_file.write("\n")
        target_file.seek(0, 2)
        target_file.write(
            f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        target_file.write(f"{file_contents}")


dir_idx = -1
file_idx = -1
file_name = ""


if "-d" in sys.argv:
    dir_idx = sys.argv.index("-d")
if "-f" in sys.argv:
    file_idx = sys.argv.index("-f")
    file_name = sys.argv[file_idx + 1]


dirs = []
if dir_idx > -1:
    if file_idx > -1:
        if dir_idx < file_idx:
            dirs = sys.argv[dir_idx + 1:file_idx]
        else:
            dirs = sys.argv[dir_idx + 1:]
    else:
        dirs = sys.argv[dir_idx + 1:]

if dirs:
    os.makedirs(os.path.join(*dirs))
if file_name:
    write_file(os.path.join(*dirs, file_name))
