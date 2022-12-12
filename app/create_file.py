from datetime import datetime

import sys
import os


command_list = sys.argv
path = ""
if "-d" in command_list:
    flag_d = command_list.index("-d")
    flag_f = len(command_list)
    if "-f" in command_list:
        flag_f = command_list.index("-f")
    dir_list = command_list[flag_d + 1: flag_f]
    for part in dir_list:
        path = os.path.join(path, part)
    try:
        os.makedirs(path)
    except OSError:
        pass

if "-f" in command_list:
    file_name = command_list[command_list.index("-f") + 1]
    tag = "w"
    if file_name in os.listdir(path):
        tag = "a"
    file_with_path = os.path.join(path, file_name)
    with open(file_with_path, tag) as file:
        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        input_text = input("Enter content line: ")
        line_number = 1
        while input_text != "stop":
            file.write(f"{line_number} {input_text}\n")
            input_text = input("Enter content line: ")
            line_number += 1
        file.write("\n")
