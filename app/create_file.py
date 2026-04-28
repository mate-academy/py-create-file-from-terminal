import os
import sys
from datetime import datetime


def parse_arguments(arguments: list) -> tuple:
    directory_list = []
    file_list = []
    current_target = None

    for arg in arguments:
        if arg == "-f":
            current_target = file_list
        elif arg == "-d":
            current_target = directory_list
        elif current_target is not None:
            current_target.append(arg)

    return directory_list, file_list


def write_to_file(file_name: str) -> None:
    # write the header content first
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    if os.path.exists(file_name):
        formatted_date = "\n" + formatted_date
        print(f"File '{file_name}' already exists. Appending content.")
    with open(file_name, "a") as file_output:
        file_output.write(f"{formatted_date}\n")
        line_counter = 1
        while True:
            input_line = input("Enter content line: ")
            if "stop" in input_line:
                break
            file_output.write(f"{line_counter} {input_line}\n")
            line_counter += 1


sys_argv = sys.argv
# if there is no argv then exit
if len(sys_argv) == 1:
    sys.exit(0)

# parsing argv and checking if there is -d or -f flag,
# and get the directory and filename
directory_list, file_list = parse_arguments(sys_argv[1:])


# if there are directories in directory list,
# then create the full path and create the directory if not exist
fullpath = ""
if len(directory_list) > 0:
    fullpath = os.path.join(*directory_list)
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)

# if there is no file in file list, then exit
if len(file_list) == 0:
    sys.exit(0)

file_name = os.path.join(fullpath, file_list[0])
write_to_file(file_name)
