import os
import sys
from datetime import datetime

if "-f" not in sys.argv:
    raise Exception("No file name passed")
file_name_position = sys.argv.index("-f") + 1
file_name = sys.argv[file_name_position]

dir_exist = False
if "-d" in sys.argv:
    dir_exist = True
    dir_position = sys.argv.index("-d") + 1
    dir_path_str = ""
    i = 0
    while True:
        if ((dir_position + i) < len(sys.argv)
                and not sys.argv[dir_position + i].startswith("-")):
            dir_path_str = (os.path.join(dir_path_str,
                                         sys.argv[dir_position + i]))
            i += 1
        else:
            break
    if not os.path.exists(dir_path_str):
        os.makedirs(dir_path_str)

if dir_exist:
    name_of_file = os.path.join(dir_path_str, file_name)
else:
    name_of_file = file_name

with open(f"{name_of_file}", "a") as f:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f.write(f"{timestamp}\n")
    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        f.write(content + "\n")
