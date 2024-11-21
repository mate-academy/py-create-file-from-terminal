import sys
import os
import datetime


enter_terminal = sys.argv
new_dir_path = ""

if "-d" in enter_terminal:
    d_index = enter_terminal.index("-d")
    for dr in enter_terminal[d_index + 1:]:
        if dr == "-f":
            break
        new_dir_path = os.path.join(new_dir_path, dr)
    os.makedirs(new_dir_path, exist_ok=True)

if "-f" in enter_terminal:
    file_name = enter_terminal[enter_terminal.index("-f") + 1]
    if new_dir_path:
        file_name = os.path.join(new_dir_path, file_name)
    with open(file_name, "a") as f:
        now = datetime.datetime.now()
        f.write(f"{now.strftime("%Y-%m-%d %X")}\n")
        num_string = 1
        while True:
            content = input("Enter content line: ")
            if content == "stop":
                f.write("\n")
                break
            f.write(f"{num_string} {content}\n")
            num_string += 1
