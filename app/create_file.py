from datetime import datetime
import os
import sys


def control_function():
    terminal = sys.argv

    if "-d" in terminal and "-f" in terminal:
        lst_path = terminal[2:-2]
        file_name = terminal[-1]
        new_path = creation_path(lst_path)
        new_dir = os.path.join(new_path, file_name)
        creation_file(new_dir)

    if "-d" in terminal:
        creation_path(terminal[2:])

    if "-f" in terminal:
        creation_file(terminal[2])


def creation_path(lst: list) -> str:
    new_path = os.path.join(*lst)

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    return new_path


def creation_file(file_name: str):
    with open(file_name, "a") as new_file:
        time_now = datetime.now()
        current_date = time_now.strftime("%Y-%m-%d %H:%M:%S")
        new_file.write(current_date + "\n")
        numb_counter = 1

        while True:
            content_line = input("Enter content line: ")

            if content_line == "stop":
                new_file.write("\n")
                exit()

            else:
                new_file.write(f"{numb_counter} {content_line}\n")
                numb_counter += 1
