import os
from datetime import datetime
from sys import argv


cmd_string = argv
cur_dir = os.getcwd()

if "-d" in cmd_string:
    d_indx = cmd_string.index("-d")
    cmd_path = []
    d_indx += 1
    while d_indx < len(cmd_string) and not cmd_string[d_indx].startswith("-"):
        cmd_path.append(cmd_string[d_indx])
        d_indx += 1
    cur_dir = os.path.join(cur_dir, *cmd_path)
    os.makedirs(cur_dir, exist_ok=True)

if "-f" in cmd_string:
    f_indx = cmd_string.index("-f")
    f_name = cmd_string[f_indx + 1]
    f_path = os.path.join(cur_dir, f_name)
    with open(f_path, "a") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")
        line = 1
        text = input("Enter content line: ")
        while text.lower() != "stop":
            f.write(f"{line} {text}\n")
            line += 1
            text = input("Enter content line: ")
        f.write("\n")
