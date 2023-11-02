import sys
import os
import datetime
from typing import Any


def together(file_path: Any) -> Any:
    with open(file_path, "a") as file:
        current_date = datetime.datetime.now()
        in_put = input("Enter content line: ")
        file.write(current_date.strftime("%d/%m/%Y %H:%M:%S") + "\n")
        while in_put != "stop":
            file.write(in_put + "\n")
            in_put = input("Enter content line: ")
        file.write("\n")
    return file


def create_file() -> None:
    term = sys.argv
    if term[1] == "-f":
        together(term[2])


def create_folder() -> None:
    term = sys.argv
    if term[1] == "-d" and term[4] != "-f":
        subdirectory_path = os.path.join(term[2], term[3])
        os.makedirs(subdirectory_path)


def create_folder_file() -> None:
    term = sys.argv
    if term[1] == "-d" and term[4] == "-f":
        subdirectory_path = os.path.join(term[2], term[3])
        os.makedirs(subdirectory_path)
        file_path = os.path.join(subdirectory_path, term[5])
        together(file_path)


create_file()
create_folder()
create_folder_file()
