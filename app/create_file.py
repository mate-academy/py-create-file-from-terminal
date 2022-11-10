import sys
import os

from datetime import datetime

command_arr = sys.argv


def create_directory(d_index, f_index=None):
    if f_index:
        path_from_command = command_arr[d_index + 1: f_index]
    else:
        path_from_command = command_arr[d_index + 1:]

    path = os.getcwd()
    for directory in path_from_command:
        path = os.path.join(path, directory)

    try:
        os.makedirs(path, exist_ok=True)
        print("Directory created successfully")
    except OSError:
        print("Directory can not be created")

    return path


def create_or_append_file(f_index, path_for_file=None):
    file_name = command_arr[f_index + 1]
    if path_for_file:
        file_name = os.path.join(path_for_file, file_name)
    current_date = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    if os.path.exists(file_name):
        mode = "a"
    else:
        mode = "w"
    with open(file_name, mode) as f:
        f.write(f"{current_date}\n")
        counter = 0
        while True:
            counter += 1
            content = input("Enter content line: ")
            if content == "stop":
                f.write("\n")
                break
            f.write(f"{counter} {content}\n")


def parsing_command():
    if "-d" in command_arr and "-f" in command_arr:
        path_for_file = create_directory(
            command_arr.index("-d"),
            command_arr.index("-f")
        )
        create_or_append_file(command_arr.index("-f"), path_for_file)
    elif "-d" in command_arr:
        create_directory(command_arr.index("-d"))
    elif "-f" in command_arr:
        create_or_append_file(command_arr.index("-f"))


if __name__ == "__main__":
    parsing_command()
