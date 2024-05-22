import datetime
import sys
import os

new_path = ""
file_name = ""
file_pos = 0
dirs = []
dir_pos = 0
lines = []
number_line = 0
input_string = ""
parent_dir = os.getcwd()


while True:
    input_string = input("Enter content line: ")
    if input_string == "stop":
        break
    number_line += 1
    lines.append(f"\n{number_line} {input_string}")

for i, arg in enumerate(sys.argv):
    if arg == "-f":
        file_name = sys.argv[i + 1]
        file_pos = i

    if arg == "-d":
        dir_pos = i

    if file_pos:
        dirs = sys.argv[dir_pos + 1 : file_pos]
    else:
        dirs = sys.argv[dir_pos + 1 :]

if dirs:
    mode = 0o666
    new_path = parent_dir

    for dir_name in dirs:
        new_path = os.path.join(new_path, dir_name.strip())
    os.makedirs(new_path, mode)

if file_name:
    if new_path:
        full_path = os.path.join(new_path, file_name)
    else:
        full_path = file_name

    with open(full_path, "a") as f:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"\n{date_str}")
        f.writelines(lines)
