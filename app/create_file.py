import sys
import os
import datetime

parent_dir = os.getcwd()


if "-f" in sys.argv:
    file_name = sys.argv[-1]
    if "-d" in sys.argv:
        directories_list = sys.argv[2:-2]
        to_join = os.path.sep.join(directories_list)
        # to_join_all = os.path.join(parent_dir, to_join)
        os.makedirs(to_join, exist_ok=True)
        file_name = os.path.join(to_join, file_name)
    with open(file_name, "a") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp}\n")
        line_num = 1
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            file.write(f"{line_num} {line}\n")
            line_num += 1
if "-d" in sys.argv and "-f" not in sys.argv:
    directories_list = sys.argv[2:-2]
    to_join = os.path.sep.join(directories_list)
    os.makedirs(to_join, exist_ok=True)
