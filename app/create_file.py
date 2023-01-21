import os
import sys
import datetime

dir_flag = False
file_flag = False
path_dir = ""

for element in sys.argv:
    if element == "-d":
        dir_flag = True
        file_flag = False
    if element == "-f":
        dir_flag = False
        file_flag = True
    if dir_flag and element != "-d" and element != "-f":
        path_dir = os.path.join(path_dir, element)
        os.makedirs(path_dir, exist_ok=True)
    if file_flag and element != "-d" and element != "-f":
        path_file = os.path.join(path_dir, element)

        with open(path_file, "a") as work_file:
            date_current = datetime.datetime.now()
            date_current = date_current.strftime("%Y-%d-%m %I:%M:%S")
            work_file.write(f"{date_current}\n")
            input_text = input("Enter content line: ")
            number_line = 0
            while input_text != "stop":
                number_line += 1
                work_file.write(f"{number_line} {input_text}\n")
                input_text = input("Enter content line: ")
            work_file.write("\n")
