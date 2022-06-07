import sys
import os
import datetime


def create_path(lst: list) -> str:
    new_path = os.path.join(*lst)

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    return new_path


def create_file(file_name: str):
    with open(file_name, "a") as new_file:
        current_time = datetime.datetime.now()
        current_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
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


def control_function():
    arguments = sys.argv

    if "-d" in arguments and "-f" in arguments:
        path_list = arguments[2:-2]
        file_name = arguments[-1]
        new_path = create_path(path_list)
        new_dir_file = os.path.join(new_path, file_name)
        create_file(new_dir_file)

    if "-d" in arguments:
        create_path(arguments[2:])

    if "-f" in arguments:
        create_file(arguments[2])
