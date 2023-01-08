import sys
import os
from datetime import datetime


def create_file_and_input_data(path_to_new_file: str) -> None:
    with open(path_to_new_file, "a") as data_to_write:
        date_now = datetime.now()
        data_to_write.write(date_now.strftime("%m-%d-%Y, %H:%M:%S") + "\n")
        line = input("Enter content line:")
        while line != "stop":
            data_to_write.write(line + "\n")
            line = input("Enter content line:")


def create_file_from_terminal() -> None:
    if "-d" in sys.argv:
        os.makedirs(os.join.path(sys.argv[2], sys.argv[3]))

        if "-f" in sys.argv:
            create_file_and_input_data(
                os.join.path(sys.argv[2], sys.argv[3], sys.argv[-1])
            )

    else:
        create_file_and_input_data(sys.argv[-1])
