import sys
import os
import datetime

dir_path = ""
file_name = None

if "-f" in sys.argv:
    file_index = sys.argv.index("-f") + 1
    file_name = sys.argv[file_index]
if "-d" in sys.argv:
    dir_index = sys.argv.index("-d") + 1
    if "-f" in sys.argv:
        end_index = sys.argv.index("-f")
    else:
        end_index = len(sys.argv)
    folders = sys.argv[dir_index:end_index]
    dir_path = os.path.join(*folders)

if dir_path:
    os.makedirs(dir_path, exist_ok=True)

if file_name:
    full_path = os.path.join(dir_path, file_name)

with open(full_path, "a") as file:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file.write(now + "\n")
    line_number = 1

    while True:
        content = input("Enter content line: ")
        if content == "stop":
            break
        file.write(f"{line_number} {content}\n")
        line_number += 1
