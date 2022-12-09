from sys import argv
import os
from datetime import datetime


input_info = argv
num_for_d = 0
row_number = 1
for item in input_info:
    if item == "-d" or num_for_d >= 1:
        num_for_d += 1

        if item != "-d" and \
                item != "-f" and \
                item != "file.txt" and \
                item not in os.getcwd():

            path = os.path.join(os.getcwd(), item)
            try:
                os.mkdir(path)
                os.chdir(item)
            except FileExistsError:
                os.chdir(item)

    if item == "-f":
        count_for_make_datetime = 0
        with open("file.txt", "a") as file:

            while True:
                content = input(f"Enter content line: {row_number} ")

                if content.lower() == "stop":
                    break

                if count_for_make_datetime == 0:
                    file.write(
                        f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                        f"Line{row_number}: {content}\n"
                    )

                    count_for_make_datetime += 1
                file.write(f"Line{row_number}: {content}\n")

                row_number += 1
            count_for_make_date = 0
