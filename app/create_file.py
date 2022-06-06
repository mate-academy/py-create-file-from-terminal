import os
import sys
from datetime import datetime


def record_file(file_name, path):
    if not os.path.exists(f"app/{path}"):
        os.makedirs(f"{path}")
    create_file_from_input(path_and_file_name=f"{path}/{file_name}")


def create_file_from_input(path_and_file_name):

    with open(f"app/{path_and_file_name}", "w", encoding="utf8") as file:

        datatime_now = datetime.now().strftime("%m-%d-%Y, %H:%M:%S\n")
        file.write(datatime_now)

        line = ""
        i = 1
        while line != "stop":
            line = input("Enter content line: ")
            file.write(f"{i} {line}\n")
            i += 1


def create_file_from_terminal():
    terminal = sys.argv
    file_name, path = "", ""
    if "-f" in terminal:
        index_f = terminal.index("-f")
        file_name = terminal[index_f + 1]
    if "-d" in terminal:
        index_d = terminal.index("-d")
        path = "/".join(terminal[index_d + 1:index_f])

    record_file(file_name, path)


create_file_from_terminal()
