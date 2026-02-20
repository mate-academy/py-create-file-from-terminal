from datetime import datetime
import sys
import os

command = sys.argv[1:]  # Видалення першого елементу

d_index = command.index("-d") if "-d" in command else None
f_index = command.index("-f") if "-f" in command else None

file_name = None
if f_index is not None:
    file_name = command[f_index + 1]
else:
    print("Error: You must provide a file name using -f")
    sys.exit()

dir_list = None
stop_index = 0
if d_index is not None:
    # if f_index is not None and f_index > d_index:
    #     stop_index = f_index
    # else:
    #     stop_index = len(command)
    stop_index = f_index if (f_index is not None
                             and f_index > d_index) else len(command)
    dir_list = command[d_index + 1:stop_index]

path = ""
if dir_list is not None:
    path = os.path.join(*dir_list)
    os.makedirs(path, exist_ok=True)

full_destination = os.path.join(path, file_name)

counter_line = 1
with open(full_destination, "a", encoding="utf-8") as file:
    file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    while True:
        file_content = input("Enter new line of content: ")
        if file_content == "stop":
            file.write("\n")
            break
        else:
            file.write(f"{counter_line} {file_content}\n")
            counter_line += 1
