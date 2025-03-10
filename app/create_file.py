import os
import sys
import datetime
# python app/create_file.py -d dir1 dir2 -f file.txt


def read_the_lines() -> list[str]:
    lines = []
    line_number = 0
    inp = ""
    while True:
        inp = input("Enter content line: ")
        if inp == "stop":
            break
        line_number += 1
        line = str(line_number) + " " + inp
        lines.append(line)
    return lines


def write_to_the_file(filename: str, path: str = "") -> None:
    with open(os.path.join(path, file_name), "a") as f:
        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        for line in lines:
            f.write(line + "\n")


directory_index = -1
file_index = -1
directories = []
args = sys.argv
current_dir = os.getcwd()

if "-d" in args:
    directory_index = args.index("-d")
if "-f" in args:
    file_index = args.index("-f")
    file_name = args[file_index + 1]
if directory_index > 0:
    if file_index > 0:
        directories = args[directory_index + 1:file_index]
        path = os.path.join(current_dir, *directories)
        if not os.path.exists(path):
            os.makedirs(path)
        lines = read_the_lines()
        write_to_the_file(file_name, path)

    else:
        directories = args[directory_index:]
        path = os.path.join(current_dir, *directories)
        os.makedirs(path)
if file_index > 0 and directory_index == -1:
    lines = read_the_lines()
    path = os.path.join(current_dir, *directories)
    write_to_the_file(file_name)
