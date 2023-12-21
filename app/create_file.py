import sys
from os import path
from datetime import datetime

FLAGS_LIST = ["-d", "-f"]


print(datetime)
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
print(dirs_list)
print(file_name)
print(full_file_path)

enter_pressed_times = 0
with open("file1.txt", "w") as f:
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{formatted_date}\n")
    while True:
        result = input("Enter content line: ")
        if result == "stop":
            break

        enter_pressed_times += 1
        f.write(f"{enter_pressed_times} {result}\n")

# print(path.join(*dirs_list, file_name))
# print(argument)
