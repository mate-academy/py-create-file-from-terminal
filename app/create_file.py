import sys
import os
from datetime import datetime

# get information from console args
i = 1
path = ""
d_flag = False
f_flag = False
file_name = ""

while i != len(sys.argv):
    if sys.argv[i] == "-d":
        if d_flag:
            raise ValueError("-d flag is already defined")
        if len(sys.argv) - 1 < i + 2:
            raise ValueError("-d flag requires two parameters")
        directory_1, directory_2 = sys.argv[i + 1:i + 3]
        path = os.path.join(directory_1, directory_2)
        os.makedirs(path)
        i += 3
        d_flag = True
    elif sys.argv[i] == "-f":
        if f_flag:
            raise ValueError("-f flag is already defined")
        if len(sys.argv) - 1 < i + 1:
            raise ValueError("-f flag requires one parameter")
        file_name = sys.argv[i + 1]
        i += 2
        f_flag = True
    else:
        raise ValueError("Invalid argument")

if not f_flag:
    raise ValueError("There is not -f flag")

path = os.path.join(path, file_name)


# Write file content
with open(path, "w") as f:
    f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
    line_counter = 1
    data = ""
    while True:
        data = input("Enter content line: ")
        if data == "stop":
            break
        f.write(f"{line_counter} {data}\n")
        line_counter += 1
