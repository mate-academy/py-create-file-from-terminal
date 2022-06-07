import sys
import os
import datetime


def control_function():
    arguments = sys.argv

    if "-d" in arguments and "-f" in arguments:
        path_list = arguments[2:-2]
        file_name = arguments[-1]
        new_path = new_path_creation(path_list)
        new_dir_file = os.path.join(new_path, file_name)
        new_file_creation(new_dir_file)

    if "-d" in arguments:
        new_path_creation(arguments[2:])

    if "-f" in arguments:
        new_file_creation(arguments[2])


def new_path_creation(lst: list) -> str:
    new_path = os.path.join(*lst)

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    return new_path


def new_file_creation(file_name: str):
    with open(file_name, "a") as new_file:
        timestamp = datetime.datetime.now()
        current_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(current_date + "\n")
        counter_of_numbers = 1

        while True:
            content_line = input("Enter content line: ")

            if content_line == "stop":
                new_file.write("\n")
                exit()

            else:
                new_file.write(f"{counter_of_numbers} {content_line}\n")
                counter_of_numbers += 1
