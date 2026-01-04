import os
import sys
from datetime import datetime

input_string = sys.argv[1:]

dirs = []
dir_exist = False
file_name = ""
file_name_exist = False

for i in input_string:
    if (i == "-d"):
        dir_exist = True
    if (i == "-f"):
        dir_exist = False
        file_name_exist = True
    if (dir_exist and i != "-d"):
        dirs.append(i)
    if (file_name_exist and i != "-f"):
        file_name = i
        file_name_exist = False

# dirs.remove("-d")
# print(dirs)
# print(file_name)

actual_directory = os.getcwd()

for director in dirs:
    actual_directory = os.path.join(actual_directory, director)

if (not os.path.exists(actual_directory)):
    os.makedirs(actual_directory)

if (file_name == ""):
    print("Please enter a file name")
    sys.exit()
else:
    new_file = os.path.join(actual_directory, file_name)

lines = []

while True:
    line = input("Enter content line: ")
    if line == "stop":
        break
    lines.append(line)

new_data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# print(new_data)
number = 1
with (open(new_file, "a") as f):
    if os.path.exists(new_file) and os.path.getsize(new_file) > 0:
        f.write("\n")
    f.write(new_data + "\n")
    for line in lines:
        f.write(str(number) + " ")
        f.write(line + "\n")
        number += 1

# print(actual_directory)
