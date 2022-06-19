import os
import sys
from datetime import datetime

if sys.argv[1] == "-d" and sys.argv[-2] != "-f":
    directory = ""

    for x in range(2, len(sys.argv)):
        directory += f"{sys.argv[x]}/"
        os.mkdir(directory)

time_now = datetime.now()
time = time_now.strftime("%Y-%m-%d %H:%M:%S")
if sys.argv[1] == "-f":
    file_name = sys.argv[2]
else:
    file_name = sys.argv[-1]

with open(file_name, 'a') as file:
    line_num = 1
    file.write(f"{time}\n")
    while True:
        line = input("Enter content line: ")
        if line == "stop":
            file.write("\n")
            break
        file.write(f"{line_num} {line}\n")
        line_num += 1
