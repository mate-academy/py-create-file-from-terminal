import datetime
import sys
import os

new_path = ""
file_name = ""
dirs = []
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

    if arg == "-d":
        dirs = sys.argv[i + 1:]

if dirs:
    mode = 0o666
    new_path = os.path.join(parent_dir, dirs[0], dirs[1])
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
