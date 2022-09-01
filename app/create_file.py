import sys
import os
import datetime


text_from_terminal = sys.argv

f_index = 0
if "-f" in text_from_terminal:
    f_index += text_from_terminal.index("-f")

d_index = 0
if "-d" in text_from_terminal:
    d_index += text_from_terminal.index("-d")


def make_only_directory():
    parent_dir = os.getcwd()
    for i in text_from_terminal[d_index + 1:len(text_from_terminal)]:
        directory = str(i)
        path = os.path.join(parent_dir, directory)
        parent_dir = path
    os.makedirs(parent_dir)


def make_only_file():
    with open(text_from_terminal[-1], "a") as f:
        now = datetime.datetime.now()
        f.write(str(now.strftime("%Y-%d-%m %H:%M:%S")) + "\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            else:
                f.write(f"{line_number} {line}\n")
                line_number += 1

        f.write("\n")


def make_directory_and_file():
    parent_dir = os.getcwd()
    for i in text_from_terminal[d_index + 1:f_index]:
        directory = str(i)
        path = os.path.join(parent_dir, directory)
        parent_dir = path
    os.makedirs(parent_dir)

    new_path = os.path.join(parent_dir, text_from_terminal[-1])
    with open(new_path, "a") as f:
        now = datetime.datetime.now()
        f.write(str(now.strftime("%Y-%d-%m %H:%M:%S")) + "\n")

        line_number = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            else:
                f.write(f"{line_number} {line}\n")
                line_number += 1

        f.write("\n")


if "-f" not in text_from_terminal:
    make_only_directory()

if "-d" not in text_from_terminal:
    make_only_file()

if "-d" and "-f" in text_from_terminal:
    make_directory_and_file()
