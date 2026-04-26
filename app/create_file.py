import os
import sys
from datetime import datetime

sys_argv = sys.argv
current_path = os.getcwd()
file_flag = ""
directory_list = []
file_name = ""
fullpath = ""

# if first flag is -d, then get new argument and
# capture second flag if any
if sys_argv[1] == "-d":
    for dir_cnt in range(2, len(sys_argv)):
        # check if there is file flag after -d flag
        if sys_argv[dir_cnt] == "-f":
            # finding any -f flag, then next argument is filename
            file_name = sys_argv[dir_cnt + 1]
            break
        directory_list.append(sys_argv[dir_cnt])
    # create subdirectory if not exist
    fullpath = os.path.join(*directory_list)
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)

if sys_argv[1] == "-f":
    # if first flag -f, then there is no directory argv
    # the next argument should be filename
    file_name = sys_argv[2]

if file_name != "":
    file_name = os.path.join(fullpath, file_name)

# write/append file
file_output = open(file_name, "a")
now = datetime.now()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
if os.path.exists(file_name):
    formatted_date = "\n" + formatted_date
file_output.write(f"{formatted_date}\n")

line_counter = 1
while True:
    input_line = input("Enter content line: ")
    if "stop" in input_line:
        break
    file_output.write(f"{line_counter} {input_line}\n")
    line_counter += 1
file_output.close()
