from datetime import datetime
import sys
import os


data = sys.argv[1:]
f_index = data.index("-f")

if "-d" in data:
    d_index = data.index("-d")
    if f_index > d_index:
        d_data = data[d_index + 1: f_index]
    else:
        d_data = data[d_index + 1:]

    path_dirs = os.path.join(*d_data)
    file_path = os.path.join(path_dirs, data[f_index + 1])
    os.makedirs(path_dirs, exist_ok=True)

else:
    file_path = os.path.join(data[f_index + 1])

current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
counter = 1
info_from_user = f"{current_time}\n"

while True:
    line_from_user = input("Enter content line: ")
    if line_from_user == "stop":
        break
    info_from_user += f"{counter} {line_from_user}\n"
    counter += 1

with open(file_path, "a") as file:
    file.write(info_from_user)
