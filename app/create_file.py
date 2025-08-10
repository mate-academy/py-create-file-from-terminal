import sys
import os
from datetime import datetime


def create_file_and_input_data(path_to_new_file: str) -> None:
    with open(path_to_new_file, "a") as data_to_write:
        date_now = datetime.now()
        data_to_write.write(date_now.strftime("%m-%d-%Y %H:%M:%S") + "\n")
        line = input("Enter content line:")
        while line != "stop":
            data_to_write.write(line + "\n")
            line = input("Enter content line:")


def create_file_from_terminal() -> None:
    list_of_input_data = sys.argv
    file_name = list_of_input_data[-1]
    directory_path = os.join.path(list_of_input_data[2], list_of_input_data[3])
    if "-d" in sys.argv:
        os.makedirs(directory_path)

        if "-f" in sys.argv:
            create_file_and_input_data(
                os.join.path(directory_path, file_name)
            )

    else:
        create_file_and_input_data(file_name)
