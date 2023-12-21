import sys
from os import path, makedirs
from datetime import datetime

FLAGS_LIST = ["-d", "-f"]

current_flag = ""
dirs_list = []
file_name = ""

for argument in sys.argv:

    if argument in FLAGS_LIST:
        current_flag = argument
        continue

    if current_flag == FLAGS_LIST[0]:
        dirs_list.append(argument)

    if current_flag == FLAGS_LIST[1]:
        file_name = argument


full_file_path = path.join(*dirs_list, file_name)

enter_pressed_times = 0
if len(dirs_list) and not path.exists(path.join(*dirs_list)):
    makedirs(path.join(*dirs_list))

if file_name:
    with open(full_file_path, "w") as source_file:
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{formatted_date}\n")
        while True:
            result = input("Enter content line: ")
            if result == "stop":
                break

            enter_pressed_times += 1
            source_file.write(f"{enter_pressed_times} {result}\n")
