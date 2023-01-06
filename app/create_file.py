import sys
import os
from datetime import datetime


list_of_input_data = sys.argv
if "-d" in list_of_input_data:
    path_to_file = os.join.path(
        list_of_input_data[0],
        list_of_input_data[2],
        list_of_input_data[3]
    )
    os.makedirs(path_to_file)

    if "-f" in list_of_input_data:
        with open(
                os.join.path(path_to_file, list_of_input_data[-1]), "a"
        ) as data_to_write:
            date_now = datetime.now()
            data_to_write.write(date_now.strftime("%m/%d/%Y, %H:%M:%S") + "\n")
            line = input("Enter content line:")
            while line != "stop":
                data_to_write.write(line + "\n")
                line = input("Enter content line:")

else:
    with open(
            os.join.path(list_of_input_data[0], list_of_input_data[-1]), "a"
    ) as data_to_write:
        date_now = datetime.now()
        data_to_write.write(date_now.strftime("%m/%d/%Y, %H:%M:%S") + "\n")
        line = input("Enter content line:")
        while line != "stop":
            data_to_write.write(line + "\n")
            line = input("Enter content line:")
