import sys
import os
import datetime
from typing import Any


cutted = sys.argv


def together(file_name: Any) -> Any:
    with open(file_name, "a") as file:
        current_date = datetime.datetime.now()
        user_input = input("Enter content line: ")
        file.write(current_date.strftime("%d/%m/%Y %H:%M:%S") + "\n")
        while user_input != "stop":
            file.write(user_input + "\n")
            user_input = input("Enter content line: ")
        file.write("\n")
    return file


def create_file() -> None:
    if "-f" in cutted and "-d" not in cutted:
        together(cutted[cutted.index("-f") + 1])


def create_folder(term_input: Any) -> None:
    os.makedirs(term_input)


def head_function() -> None:
    if "-d" in cutted:
        if "-f" in cutted:
            d_symbol = cutted.index("-d")
            f_symbol = cutted.index("-f")
            if f_symbol > d_symbol:
                print(cutted[d_symbol + 1:f_symbol])
                unpacking = os.path.join(*cutted[d_symbol + 1:f_symbol])
                create_folder(unpacking)
                together(cutted[f_symbol + 1])
            if d_symbol > f_symbol:
                together(sys.argv[f_symbol + 1])
                create_folder(os.path.join(*cutted[d_symbol + 1::]))
        create_folder(os.path.join(*cutted[cutted.index("-d") + 1::]))


head_function()
create_file()
