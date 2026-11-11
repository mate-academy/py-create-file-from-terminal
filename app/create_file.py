import datetime
import sys
import os


args_list = sys.argv[1:]
file_position = 1000
directory_list = ""
folder_path = ""
file_name = ""
full_path = ""

if "-f" in args_list:
    file_position = args_list.index("-f")
    file_name = args_list[file_position + 1]
if "-d" in args_list:
    directory_position = args_list.index("-d")
    if directory_position < file_position:
        directory_list = args_list[directory_position + 1: file_position]
    elif directory_position > file_position:
        directory_list = args_list[directory_position + 1:]

    folder_path = "/".join(directory_list)
    os.makedirs(folder_path, exist_ok=True)


if "-f" in args_list and "-d" in args_list:
    full_path = os.path.join(folder_path, file_name)
elif "-f" in args_list:
    full_path = file_name

if "-f" in args_list:
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
