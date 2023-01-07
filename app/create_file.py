import sys
import os
from datetime import datetime


def create_file_and_input_data(path_to_new_file: str) -> None:
    with open(path_to_new_file, "a") as data_to_write:
        date_now = datetime.now()
        data_to_write.write(date_now.strftime("%m/%d/%Y, %H:%M:%S") + "\n")
        line = input("Enter content line:")
        while line != "stop":
            data_to_write.write(line + "\n")
            line = input("Enter content line:")


def create_file_from_terminal() -> None:
    list_of_input_data = sys.argv
    if "-d" in list_of_input_data:
        path_to_file = os.join.path(
            list_of_input_data[2],
            list_of_input_data[3]
        )
        os.makedirs(path_to_file)

        if "-f" in list_of_input_data:
            create_file_and_input_data(
                os.join.path(path_to_file, list_of_input_data[-1])
            )

    else:
        create_file_and_input_data(list_of_input_data[-1])
