import os
import sys
from datetime import datetime


def record_file(file_name, path):
    if not os.path.exists(f"{path}"):
        os.makedirs(f"{path}")
    create_file_from_input(path_and_file_name=f"{path}/{file_name}")


def create_file_from_input(path_and_file_name):

    with open(f"{path_and_file_name}", "a+", encoding="utf8") as file:

        datatime_now = datetime.now().strftime("%m-%d-%Y, %H:%M:%S\n")
        file.write(datatime_now)

        number_line = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{number_line} {line}\n")
            number_line += 1


def create_file_from_terminal():
    terminal = sys.argv
    file_name, path = "", ""
    index_f = -1
    if "-f" in terminal:
        index_f = terminal.index("-f")
        file_name = terminal[index_f + 1]
    if "-d" in terminal:
        index_d = terminal.index("-d")
        path = "/".join(terminal[index_d + 1:index_f])
    print(file_name, path)
    record_file(file_name, path)


create_file_from_terminal()
