import sys
import os
from datetime import datetime


def create_file() -> None:
    cmd_line = sys.argv
    path = os.getcwd()
    if "-d" in cmd_line and cmd_line[1] == "-d":
        d_line = []
        for flag in cmd_line[2:]:
            if flag != "-f":
                d_line.append(flag)
            else:
                break
        for directory in d_line:
            path = os.path.join(path, directory)
        os.makedirs(path, exist_ok=True)
    if "-f" in cmd_line:
        flag_end_index = cmd_line.index("-f") - len(cmd_line)
        if flag_end_index != -2:
            return
        file_path = os.path.join(path, cmd_line[-1])
        file_exists = os.path.exists(file_path)
        with open(f"{file_path}", "a") as file:
            if file_exists:
                file.write("\n")
            time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{time_stamp}\n")
            line_number = 1
            while True:
                line = input("Enter content line: ")
                if line != "stop":
                    file.write(f"{line_number} {line}\n")
                    line_number += 1
                else:
                    break


create_file()
