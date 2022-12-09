from sys import argv
import os
from datetime import datetime


def make_directors(input_info: list) -> None:
    num_for_make_directory = 0
    num_for_make_file = 0

    while True:
        for item in input_info:
            if item == "-d" or num_for_make_directory >= 1:
                num_for_make_directory += 1
                if item not in os.getcwd() and\
                        item != "-d" and\
                        item != "file.txt":

                    path = os.path.join(os.getcwd(), item)
                    try:
                        os.mkdir(path)
                        os.chdir(item)
                    except FileExistsError:
                        os.chdir(item)

            if item == "-f" or num_for_make_file > 0:
                num_for_make_file += 1
                make_file(item)
                if item == input_info[-1] and "-f" in input_info:
                    return


def make_file(file_info: str) -> None:
    count_for_make_datetime = 0
    variable_for_rows = 1
    if file_info == "-f":
        return
    with open("file.txt", "a") as file:

        while True:
            content = input(f"Enter content line: {variable_for_rows} ")

            if content.lower() == "stop":
                break

            if count_for_make_datetime == 0:
                file.write(
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                )
                count_for_make_datetime += 1
            file.write(f"Line{variable_for_rows}: {content}\n")
            variable_for_rows += 1


make_directors(argv)
