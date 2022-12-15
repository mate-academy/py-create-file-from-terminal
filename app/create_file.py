import datetime
import os
import sys


command_line = sys.argv
current_directory = os.getcwd()

if "-d" in command_line:
    for line in range(2, len(command_line)):
        if command_line[line] == "-f":
            break
        current_directory = os.path.join(current_directory, command_line[line])
    os.makedirs(current_directory)

if "-f" in command_line:
    file_path_and_name = os.path.join(current_directory, command_line[-1])
    with open(f"{file_path_and_name}", "a") as f:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{current_date} \n")
        line_number = 1
        while True:
            input_line = input("Enter content line: ")
            if input_line == "stop":
                break
            f.write(f"{line_number} {input_line} \n")
            line_number += 1
