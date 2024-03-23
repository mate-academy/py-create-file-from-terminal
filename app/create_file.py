import sys
import os
import datetime


def write_info(file_name: str) -> None:

    line = input("Enter content line: ")
    counts = 1
    with open(file_name, "a") as file_open:
        if os.stat(file_name).st_size != 0:
            file_open.write("\n")
        counts = 1
        while line != "stop":
            if counts == 1:
                file_open.write(datetime.datetime.now()
                                .strftime("%Y-%m-%d %H:%M:%S")
                                + "\n")
            file_open.write(f"{counts} {line}\n")
            line = input("Enter content line: ")
            counts += 1


current_path = os.path.dirname(os.path.abspath(__file__))
current_messege = sys.argv
new_path = current_path

try:
    flag_file_pos = current_messege.index("-f")
except IndexError:
    quit("I don't have file to write, so bay.")
else:
    new_file_name = current_messege[flag_file_pos + 1]

try:
    flag_dir_pos = current_messege.index("-d")
except IndexError:
    pass
else:
    while (flag_dir_pos < len(current_messege) - 1
           and current_messege[flag_dir_pos + 1] != "-f"):
        new_path = os.path.join(new_path, current_messege[flag_dir_pos + 1])
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        flag_dir_pos += 1

try:
    _ = open(os.path.join(new_path, new_file_name), "x")
except IOError:
    pass
write_info(os.path.join(new_path, new_file_name))
