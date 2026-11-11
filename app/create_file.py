import datetime
import sys
from typing import Union
import os


def arg_parsing(args_list: list) -> Union[str, list, None]:
    file_name = ""
    directory_list = []
    file_position = 10000
    if "-f" in args_list:
        file_position = args_list.index("-f")
        file_name = args_list[file_position + 1]
    if "-d" in args_list:
        directory_position = args_list.index("-d")
        if directory_position < file_position:
            directory_list = args_list[directory_position + 1: file_position]
        elif directory_position > file_position:
            directory_list = args_list[directory_position + 1:]

    return file_name, directory_list


# directory creation
def create_dir(directory_list: list) -> str:
    folder_path = os.path.join(*directory_list)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


# write to file
def write_file(full_path: str) -> None:
    user_input = ""
    with open(full_path, "a") as file:
        if os.path.getsize(full_path) > 0:
            file.write("\n")
        current_time = datetime.datetime.now()
        file.write(current_time.strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line_number = 1
        while user_input != "stop":
            user_input = input("Enter content line: ")
            if user_input == "stop":
                break
            file.write(str(line_number) + " " + user_input + "\n")
            line_number += 1


if "-f" in sys.argv and "-d" in sys.argv:
    file_name, directory_list = arg_parsing(sys.argv)
    folder_path = create_dir(directory_list)
    full_path = os.path.join(folder_path, file_name)
elif "-f" in sys.argv:
    file_name, directory_list = arg_parsing(sys.argv)
    full_path = file_name
else:
    file_name, directory_list = arg_parsing(sys.argv)
    create_dir(directory_list)

# file writing
if "-f" in sys.argv:
    write_file(full_path)
