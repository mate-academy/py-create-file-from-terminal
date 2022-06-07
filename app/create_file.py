import os
import sys
import datetime


def main():
    arguments = sys.argv
    if "-d" in arguments and "-f" in arguments:
        path_list = arguments[2:-2]
        file_name = arguments[-1]
        second_path = new_path(path_list)
        new_dir_file = os.path.join(second_path, file_name)
        new_file(new_dir_file)

    if "-d" in arguments:
        new_path(arguments[2:])

    if "-f" in arguments:
        new_file(arguments[2])


def new_path(lst: list) -> str:
    second_path = os.path.join(*lst)

    if not os.path.exists(second_path):
        os.makedirs(second_path)

    return second_path


def new_file(file_name: str):
    with open(file_name, "a") as another_file:
        timestamp = datetime.datetime.now()
        current_date = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        another_file.write(current_date + "\n")
        counter_of_numbers = 1

        while True:
            content_line = input("Enter content line: ")

            if content_line == "stop":
                another_file.write("\n")
                exit()

            else:
                another_file.write(f"{counter_of_numbers} {content_line}\n")
                counter_of_numbers += 1
