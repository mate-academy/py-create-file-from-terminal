import sys
import datetime
import os
from typing import Any


def create_file() -> Any:
    arguments = sys.argv
    dir_path = ""
    file_name = ""

    if "-d" in arguments:
        flag_d = arguments.index("-d")
        next_flag = arguments.index("-f")\
            if "-f" in arguments\
            else len(arguments)
        dir_path = "/".join(arguments[flag_d + 1 : next_flag])
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in arguments:
        flag_f = arguments.index("-f")
        file_name = arguments[flag_f + 1]

    file_path = f"{dir_path}/{file_name}" if dir_path else file_name

    if not file_name:
        print("Dir crated")
    else:
        with open(file_path, "a") as file:
            print("For stop input please write stop")
            date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"{date_str}\n")
            while True:
                line = input("Print your massege: ")
                if line.lower() == "stop":
                    break
                file.write(f"{line}\n")
                file.write("\n")


create_file()
